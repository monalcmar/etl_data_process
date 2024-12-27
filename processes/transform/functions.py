# Importar librerias python
import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# from logger.logger import logger

# logger = logger()

import dependencies as dp

def all_columns_to_str (df):
    '''
    This function cleans and transforms a DataFrame `df` with the following steps:
    
    1. Drops rows where all columns contain NaN values.
    2. Filters out rows that contain the text '***' in any text column.
    3. Converts float-type columns to integer type (Int64) if all non-NaN values in the column are integers.
    4. Converts all columns to strings (`str`), replacing NaN values with empty strings and removing leading and trailing whitespace.

    Parameters:
        - df (pd.DataFrame): The DataFrame to be transformed and cleaned.

    Returns:
        - pd.DataFrame: The cleaned and transformed DataFrame.
    '''
    # Drop rows where all columns are NaN
    df.dropna(how='all', inplace=True)

    # Apply the filter to remove rows that contain '***' in any text column
    for column in df.select_dtypes(include='object').columns:
        df = df[~df[column].astype(str).str.contains(r'\*\*\*', na=False)]
    
    # cheach each column of float type to check if it can be integer
    for column in df.select_dtypes(include=["float"]).columns:
        # verifies if each non nan values of the column are integers
        if df[column].dropna().apply(float.is_integer).all():
            # Converts the column to int, keeping NaN values
            df[column] = df[column].astype("Int64")

    for column in df.select_dtypes(include=["object"]).columns:
    # Convert values that can be interpreted as floats to int, keep NaN or non-numeric values
        df[column] = df[column].apply(lambda x: str(x) if pd.isna(x) else int(x) if isinstance(x, float) else x)
    
    for column in df.columns:
        df[column] = df[column].astype(str)
        df[column] = df[column].replace('nan', None)
        df[column] = df[column].replace('<NA>', None)
        df[column] = df[column].replace('NaT', None)
        df[column] = df[column].str.strip()


    return df


# Check null values

def check_nulls(df, dict_info):
    '''
    This function verifies null values in a dataframe that cannot be null.

        Input:
            - df (DataFrame): DataFrame to get rid of null values in specific columns.
            - dict_info (Dictionary): Dictionary containing the column information and their rules.
        
        Output: 
            - df (DataFrame): DataFrame with no null values in specific columns that are not allowed to be null.
            - df_invalid_rows (DataFrame): DataFrame containing invalid rows with reasons for violations.
    '''
    
    # Crear una columna 'Reason' vacía para almacenar los motivos
    df['Reason'] = ""

    # Inicializar un diccionario para rastrear las columnas con valores nulos
    null_columns_per_row = {}

    # Verificar las filas según las reglas de dict_info
    for column, rules in dict_info.items():
        # Si la columna no permite valores nulos
        if not rules['nullable']:
            # Encontrar las filas que tienen valores nulos en la columna actual
            null_rows = df[column].isnull()

            # Rastrear las columnas que generan problemas en cada fila
            for index in df[null_rows].index:
                if index not in null_columns_per_row:
                    null_columns_per_row[index] = []
                null_columns_per_row[index].append(column)

    # Actualizar la columna 'Reason' con una frase consolidada por fila
    for index, columns in null_columns_per_row.items():
        df.loc[index, 'Reason'] = (
            f"The columns {', '.join([f"'{col}'" for col in columns])} do not allow null values."
        )

    # Filtrar las filas inválidas y eliminar la columna Reason del DataFrame limpio
    df_invalid_rows = df[df['Reason'] != ""].copy()
    df = df[df['Reason'] == ""].drop(columns=['Reason'])

    # Log de errores
    if not df_invalid_rows.empty:
        dp.logger.error(f'There is constraint violation in null values for table.')
    else:
        dp.logger.info(f'There is no constraint violation in null values for table.')

    return df, df_invalid_rows

# Check data types

def check_data_types(df, dict_info, df_invalid=None):
    '''
    This function verifies the data types of columns in a DataFrame and converts them to the required types as per the provided dictionary.
    
    Input:
        - df (DataFrame): The dataframe containing the data.
        - dict_info (Dictionary): Dictionary with column information, including expected data types.
        - df_invalid (DataFrame, optional): DataFrame to append rows with invalid data.
    
    Output: 
        - df (DataFrame): DataFrame with columns converted to the specified data types.
        - df_invalid_rows (DataFrame): DataFrame with rows where data type conversion failed or violated the rules.
    '''
    
    if df_invalid is None:
        df_invalid = pd.DataFrame()  # Initialize df_invalid if not provided

    # Loop through each column and validate the data type
    for column, rules in dict_info.items():
        expected_type = rules['data_type']  # Get the expected data type for the column
        
        try:
            # Try to convert the column to the expected type
            if expected_type == 'datetime64[ns]':  # Special handling for datetime conversion
                df[column] = pd.to_datetime(df[column], errors='coerce')  # Convert and coerce errors to NaT
            elif expected_type == 'timedelta64[ns]':
                df[column].astype(str).replace('NaT', None)
            elif expected_type == str:
                    df[column] = df[column].astype(expected_type).replace('None', None)
            else:
                df[column] = df[column].astype(expected_type)  # Convert to the expected type

        except Exception as e:
            # Identify rows that failed type conversion
            if expected_type == 'datetime64[ns]':
                invalid_rows = df[pd.to_datetime(df[column], errors='coerce').isna() & pd.notnull(df[column])]
            else:
                invalid_rows = df[~df[column].apply(lambda x: isinstance(x, (int, float)) if expected_type in ['int64', 'float64'] else True) & pd.notnull(df[column])]
            
            # Add reason for invalid rows
            if not invalid_rows.empty:
                invalid_rows['Reason'] = f"The column '{column}' has values that cannot be converted to {expected_type}."
                df_invalid = pd.concat([df_invalid, invalid_rows])
            
            # Attempt coercion to NaN for problematic values
            if expected_type == 'datetime64[ns]':
                df[column] = pd.to_datetime(df[column], errors='coerce')
            else:
                df[column] = pd.to_numeric(df[column], errors='coerce')

    return df, df_invalid

from utils.functions import build_upload_query
from model.model_info import gold_properties
from model.gold_schema_mappings import fkey_mapping

def assing_foreig_keys (tbl_gold, df_silver, fk_relations, conn):
    '''
    This function assign Foreign Keys columns to a dataframe acording to its relations on a ddbb model. 

    input:
        - tbl_gold (str): Name of the table which Fkeys are assigned.
        - df_silver (DataFrame): df which Fkeys are goint to be assigned.
        - fk_relations (Dictionary): Dictionary with the Foreign Keys information. 

    output:
        - df_fkeys_assigned (DataFrame): The python DataFrame with all its Foreign Keys assigned.
    '''
    # define empty df to store df with fkeys assigned
    df_merge_fkeys = df_silver
    
    for fkey_name, fkey_details in fk_relations.items():
        dp.logger.info(f"Assigning column '{fkey_name}' to table '{tbl_gold}' stracted from Silver Schema.")

        # Assign keys from the dictionary of each Fkey dictionary
        tbl = fkey_details['tbl']
        select_columns = fkey_details['select_columns']
        left_on = fkey_details['left_on']
        right_on = fkey_details['right_on']
        pk_to_fk = fkey_details['pk_to_fk']

        # Construct query for the foreign table
        query = build_upload_query(
            table_name=tbl,
            key_columns=select_columns,
            date_column=None
        )

        foreing_tbl = pd.read_sql(query, con=conn)

        # IMPORTANTE: Comprobar que los tipos de datos en left_on y right_on son idénticos este codigo se rompio por los rights_on cambiados a listas.

        ## APAÑO DE LO IMPORTANTE ARRIBA

        # Define suffixes when principal and foreign table are merge    
        merge_suffixes = ("_silver", "_foreign")

        ####### APAÑO #######
        if tbl_gold in {'BonosTrabajadas', 'Invertidas'} and fkey_name == 'FkOrdenReparacion':
            df_merge_fkeys[left_on] = df_merge_fkeys[left_on].astype('Int64').astype(str)
            df_merge_fkeys[left_on] = df_merge_fkeys[left_on].replace('<NA>', None)

        # Realizar el merge acumulativo
        df_merge_fkeys = pd.merge(
            df_merge_fkeys,
            foreing_tbl,
            left_on=left_on,
            right_on=right_on,
            how='left',
            suffixes=merge_suffixes
        )

        # Renaming columns acording to 'pk_to_fk'
        df_merge_fkeys = df_merge_fkeys.rename(columns=pk_to_fk)

        # Identify duplicate foreign columns after merge
        duplicated_columns = [col for col in df_merge_fkeys.columns if col.endswith("_foreign")]
        for col in duplicated_columns:
            dp.logger.info(f"Removing unnecessary foreign column '{col}' from the table '{tbl_gold}'.")
            df_merge_fkeys = df_merge_fkeys.drop(columns=[col])

        # Restore original silver column names (if applicable)
        renamed_columns = {col: col.replace("_silver", "") for col in df_merge_fkeys.columns if col.endswith("_silver")}
        
        if renamed_columns:
            dp.logger.info(f"Renaming columns to their original names: {renamed_columns}")
            df_merge_fkeys = df_merge_fkeys.rename(columns=renamed_columns)

    ##### APAÑO #### ¡Creo que ya no es necesario, pero verificar, porque esta corregido en el modelo!
    if tbl_gold == 'Vehiculos':
        df_merge_fkeys = df_merge_fkeys.rename(columns={'FechaUltimo':'FechaUltimaVisita'})    

    df_merge_fkeys = df_merge_fkeys[gold_properties[tbl_gold].keys()]

    dp.logger.debug(f"Foreign key assignment for table '{tbl_gold}' completed.")

    return df_merge_fkeys