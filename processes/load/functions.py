# Import python libraries
import os
import sys
import pandas as pd
import numpy as np
# from pathlib import Path
from datetime import date, timedelta
from sqlalchemy import text

import dependencies as dp

from model.gold_schema_mappings import column_name_mapping
from utils.functions import create_combined_key, build_upload_query


# === Upload New Data ===

def upload_new_data_master (df, table_name, key_column, engine):
    '''
    Process new values: 
        - Get existing values from the database.
        - Identify new values in the dataframe.
        - Write new values to the database table.

    input: 
        table_name (str): name of the table in the database.
        df (DataFrame): dataframe to be compared with existing values.
        key_column (str): key column name in the dataframe and table database to compare.
        engine (SQLAlchemy engine): database connection.

    output:
        None
    '''
    # Get existing values from the database
    query = f'SELECT "{key_column}" FROM "{table_name}"'
    existing_values = pd.read_sql(query, con=engine)[key_column].tolist()

    # Get new data by comparing dataframe with existing values
    df_new_data = df[~df[key_column].isin(existing_values)]

    # Write new values to the database
    if not df_new_data.empty:
        df_new_data.to_sql(table_name, con=engine, if_exists='append', index=False)




def upload_new_data_fact (df, table_name, key_column, date_column, engine):
    '''
    Process new values: 
        - Get existing values from the database.
        - Identify new values in the dataframe.
        - Write new values to the database table.

    input: 
        table_name (str): name of the table in the database.
        df (DataFrame): dataframe to be compared with existing values.
        key_column (str): key column name in the dataframe and table database to compare.
        date_column (str): date column name in the dataframe and table database to compare.
        engine (SQLAlchemy engine): database connection.

    output:
        None
    '''
    # get date range
    current_date = date.today()
    min_date = current_date - timedelta(days=120)

    current_date = current_date.strftime('%Y-%m-%d')
    min_date = min_date.strftime('%Y-%m-%d')
    
    # Get existing values from the database
    query = f'''
        SELECT "{key_column}", "{date_column}"
        FROM "{table_name}" 
        WHERE "{date_column}" BETWEEN '{min_date}' AND '{current_date}'
        '''
    existing_values = pd.read_sql(query, con=engine)

    # Get new data by comparing dataframe with existing values

    # Generate combined keys for comparison to identify new data
    df = df.assign(
        combined_key=df[key_column].astype(str) + "_" + df[date_column].astype(str)
    )
    existing_values = existing_values.assign(
        combined_key=existing_values[key_column].astype(str) + "_" + existing_values[date_column].astype(str)
    )

    # Filter rows in df that are not in existing_values
    df_new_data = df[~df['combined_key'].isin(existing_values['combined_key'])]

    # Drop the temporary 'combined_key' column before saving new values
    df_new_data = df_new_data.drop(columns='combined_key')
    existing_values = existing_values.drop(columns='combined_key')

    # Write new values to the database
    if not df_new_data.empty:
        df_new_data = df_new_data.sort_values(date_column, ascending=True)
        df_new_data.to_sql(table_name, con=engine, if_exists='append', index=False)

    # Optional: return df_new_data if needed for further processing or testing
    # return df_new_data


def upload_new_data_fact_mult (df, table_name, key_columns, date_column, engine):
    '''
    Process new values: 
        - Get existing values from the database.
        - Identify new values in the dataframe.
        - Write new values to the database table.

    input: 
        table_name (str): name of the table in the database.
        df (DataFrame): dataframe to be compared with existing values.
        key_columns (list): list ok key column names in the dataframe and table database to compare.
        date_colum (str): date column name in the dataframe and table database to compare.
        engine (SQLAlchemy engine): database connection.

    output:
        None
    '''

    # get date range
    current_date = date.today()
    min_date = current_date - timedelta(days=120)

    current_date = current_date.strftime('%Y-%m-%d')
    min_date = min_date.strftime('%Y-%m-%d') # pd.to_datetime(df[date_column], format='%Y-%m-%d', errors='coerce').min().strftime('%Y-%m-%d')
    
    # Get existing values from the database
    query = f'''
        SELECT "{key_columns[0]}", "{key_columns[1]}", "{date_column}"
        FROM "{table_name}" 
        WHERE "{date_column}" BETWEEN '{min_date}' AND '{current_date}'
        '''
    existing_values = pd.read_sql(query, con=engine)#[key_column].tolist()

    # Get new data by comparing dataframe with existing values

    # Generate combined keys for comparison to identify new data
    df = df.assign(
        combined_key=df[key_columns[0]].astype(str) + "_" + 
                    df[key_columns[1]].astype(str) + "_" + 
                    df[date_column].astype(str)
    )

    # Crear 'combined_key' en existing_values
    existing_values = existing_values.assign(
        combined_key=existing_values[key_columns[0]].astype(str) + "_" + 
                    existing_values[key_columns[1]].astype(str) + "_" + 
                    existing_values[date_column].astype(str)
    )

    # Filter rows in df that are not in existing_values
    df_new_data = df[~df['combined_key'].isin(existing_values['combined_key'])]

    # Drop the temporary 'combined_key' column before saving new values
    df_new_data = df_new_data.drop(columns='combined_key')
    existing_values = existing_values.drop(columns='combined_key')

    # Write new values to the database
    if not df_new_data.empty:
        df_new_data = df_new_data.sort_values(date_column, ascending=True)
        df_new_data.to_sql(table_name, con=engine, if_exists='append', index=False)

    # Optional: return df_new_data if needed for further processing or testing
    # return df_new_data

# GENERALIZACIÓN DE ESTAS TRES FUNCIONES ANTERIORES 
def get_new_data (df, table_name, key_columns, date_column, engine):
    '''
    Process new values: 
        - Get existing values from the database.
        - Identify new values in the dataframe.

    input: 
        - table_name (str): name of the table in the database.
        - df (DataFrame): dataframe to be compared with existing values.
        - key_columns (list): list ok key column names in the dataframe and table database to compare.
        - date_colum (str): date column name in the dataframe and table database to compare.
        - engine (SQLAlchemy engine): database connection.

    output:
        - df_new_data (DataFrame): Dataframe with new indentified data.
    '''
   
    # Get existing values from the database
    query = build_upload_query(
        table_name=table_name,
        key_columns = key_columns,
        date_column = date_column
        )

    df_existing_data = pd.read_sql(query, con=engine)#[key_column].tolist()

    # Get new data by comparing dataframe with existing values

    # Generate combined keys for comparison to identify new data
    df = df.assign(
        combined_key=create_combined_key(
            df=df,
            key_columns=key_columns,
            date_column=date_column)
        )

    # Crear 'combined_key' en existing_values
    df_existing_data = df_existing_data.assign(
        combined_key=create_combined_key(
            df=df_existing_data,
            key_columns=key_columns,
            date_column=date_column)
        )

    # Filter rows in df that are not in existing_values
    df_new_data = df[~df['combined_key'].isin(df_existing_data['combined_key'])]

    # Drop the temporary 'combined_key' column before saving new values
    df_new_data = df_new_data.drop(columns='combined_key')
    df_existing_data = df_existing_data.drop(columns='combined_key')

    return df_new_data, df_existing_data

def upload_new_data(df_new_data, table_name, engine, date_column=None):
    ''''''
    if date_column:
        df_new_data = df_new_data.sort_values(date_column, ascending=True)
    
    df_new_data.to_sql(table_name, con=engine, if_exists='append', index=False)    

# === Update Modified Data ===

def get_modified_data (df_new_data, df_ref_data, key_columns, date_column=None):
    '''
    Identifies and retrieves modified rows by comparing a DataFrame with new data 
    against a reference DataFrame representing the current state in the database.

    Parameters:
        - df_new_data (DataFrame): DataFrame containing the new data to compare.
        - df_ref_data (DataFrame): DataFrame with the reference data from the database.
        - key_columns (list of str): List of column names used to generate a unique 
          combined key for identifying rows.
        - date_column (str, optional): Name of a date column included in the combined 
          key for more precise row identification (default is None).

    Returns:
        - df_mod_data (DataFrame): A DataFrame containing only the rows with modified 
          data, where any column differs between the new and reference data. 
    '''

    # create combined_key for each df 
    df_new_data = df_new_data.assign(
        combined_key=create_combined_key(
            df=df_new_data,
            key_columns=key_columns,
            date_column=date_column)
        )

    df_ref_data = df_ref_data.assign(
        combined_key=create_combined_key(
            df=df_ref_data,
            key_columns=key_columns,
            date_column=date_column)
        )

    merge_data = df_new_data.merge(
        df_ref_data, on='combined_key',
        suffixes=('_new', '_ref')
        )

    # Make sure both DataFrames have the same column names and index
    new_merge_data = merge_data.filter(regex='_new$').sort_index(axis=1)
    df_ref_data = merge_data.filter(regex='_ref$').sort_index(axis=1)

    # Otherwise column names are adjusted
    new_merge_data.columns = new_merge_data.columns.str.replace('_new$', '', regex=True)
    df_ref_data.columns = df_ref_data.columns.str.replace('_ref$', '', regex=True)

    # Normalize data: fill None/NaN and convert to consistent types
    new_merge_data = new_merge_data.fillna("").astype(str)
    df_ref_data = df_ref_data.fillna("").astype(str)


    # Compare rows where there are differences
    df_mod_data = merge_data[(new_merge_data != df_ref_data).any(axis=1)]

    return df_mod_data

def update_modified_data (df_mod_data, key_columns, db_tbl_name, conn):
    '''
    Updates rows in a database table based on modified data provided in a Pandas DataFrame.

    imput:
        - df_mod_data (DataFrame): Dataframe with rows of data that has been modified.
        - key_columns (list of str): List of column names used to generate a unique 
          combined key for identifying rows. 
        - bd_tbl_name (str): String with the name of the database table name to be updated. 
        - conn (sqlalchemy.engine.base.Connection): Database base engine base connection.
    
    output:
        None
    '''
    for _, fila in df_mod_data.iterrows():
        # print(f"Procesando fila {_}:")
        # print(fila)

        # Dic of values fot SET CLause (without "_new")
        valores = {
            col.replace('_new', ''): fila[col]
            for col in df_mod_data.filter(regex='_new$').columns
        }

        # print("Valores para SET:", valores)

        # SET and WHERE Clauses
        set_clause = ', '.join([f'"{col}" = :{col}' for col in valores.keys()])
        where_clause = " AND ".join(
            [f'"{key}" = :key_{key}' for key in key_columns]
        )
        query = f'UPDATE "{db_tbl_name}" SET {set_clause} WHERE {where_clause}'

        # Create query parameters
        params = valores.copy()
        params.update({
            f'key_{key}': fila[f"{key}_new"] for key in key_columns
        })

    # print("Query generado:", query)
    # print("Parámetros generados:", params)

        # Execute query
        # with conn as conn:
        #     conn.begin()
        conn.execute(text(query), params)
        conn.commit()


def get_new_data_gold(df_silver, table_name, engine, column_name_mapping, fkey_mapping, table_relations):
    """
    Identify new rows in Silver DataFrame compared to Gold DataFrame.

    Parameters:
        - df_silver (DataFrame): Silver DataFrame with potential new rows.
        - table_name (str): Gold table name.
        - engine: SQLAlchemy engine for Gold schema.
        - column_name_mapping (dict): Mapping of column names from Silver to Gold schema.
        - fkey_mapping (dict): Foreign key mappings for Gold schema.
        - table_relations (dict): Contains old key columns mapping for Gold schema.

    Returns:
        - DataFrame: New rows to insert into the Gold table.
    """
    # Map columns from Silver to Gold schema
    mapped_columns = column_name_mapping.get(table_name, {})
    if not mapped_columns:
        raise ValueError(f"No column mapping found for table {table_name}")

    # Extract old key columns and date column from table_relations
    old_key_columns = []
    date_column = None

    # Iterate through table_relations categories and tables
    for __, relations in table_relations.items():
        for relation in relations:
            if relation['tbl_gold'] == table_name:
                old_key_columns = relation.get('key_columns', [])
                date_column = relation.get('date_column', None)
                break  # Exit inner loop once the table is found
        if old_key_columns:  # Exit outer loop if the table is found
            break

    if not old_key_columns:
        raise ValueError(f"No key columns found for table {table_name} in table_relations")

    combined_key_columns = []
    gold_additional_columns = {}  # To store parent table key mapping for Gold

    for old_key in old_key_columns:
        if mapped_columns.get(old_key) is None:
            # If the key is mapped to None, use FK and parent table to fetch the old key
            fk_info = fkey_mapping.get(table_name, {}).get(old_key)
            if not fk_info:
                raise ValueError(f"No FK mapping found for key column '{old_key}' in table {table_name}")
            
            parent_tbl_gold, parent_pkey_column = fk_info
            fk_in_gold = next(
                (fk for fk, (parent_table, _) in fkey_mapping.get(table_name, {}).items() if parent_table == parent_tbl_gold),
                None
            )
            if not fk_in_gold:
                raise ValueError(f"No FK column found in {table_name} for parent table {parent_tbl_gold}")
            
            dp.logger.info(f"Fetching old key '{old_key}' using FK '{fk_in_gold}' -> '{parent_pkey_column}' from '{parent_tbl_gold}'")
            
            parent_query = f'SELECT "{parent_pkey_column}", "{old_key}" FROM "gold"."{parent_tbl_gold}"'
            parent_df = pd.read_sql(parent_query, con=engine)
            
            gold_additional_columns[old_key] = (fk_in_gold, parent_pkey_column, parent_df)
            combined_key_columns.append(old_key)
        else:
            # Otherwise, use the mapped column directly
            combined_key_columns.append(mapped_columns[old_key])

    if date_column:
        # Add the date column to the comparison keys if it exists
        mapped_date_column = mapped_columns.get(date_column)
        if mapped_date_column:
            combined_key_columns.append(mapped_date_column)
        else:
            dp.logger.warning(f"Date column '{date_column}' is not mapped for table '{table_name}'")

    if not combined_key_columns:
        raise ValueError(f"No valid key columns found for table {table_name}")

    # Build query to fetch Gold data
    query = (
        f"SELECT {', '.join([f'\"{col_gold}\"' for __, col_gold in mapped_columns.items() if col_gold is not None])}"
        + f" FROM \"gold\".\"{table_name}\""
        + f" JOIN \"gold\".\"{parent_tbl_gold}\" ON \"gold\".\"{parent_tbl_gold}.\""
    )
    gold_df = pd.read_sql(query, con=engine)

    # Add old key columns from parent Gold tables to gold_df
    for old_key, (fk_in_gold, parent_pkey_column, parent_df) in gold_additional_columns.items():
        dp.logger.info(f"Adding old key '{old_key}' from parent table via '{fk_in_gold}'")
        gold_df = gold_df.merge(
            parent_df,
            how="left",
            left_on=fk_in_gold,
            right_on=parent_pkey_column,
            suffixes=("", f"_{old_key}")
        )
        gold_df.rename(columns={f"{old_key}_{old_key}": old_key}, inplace=True)

    # Normalize Gold DataFrame dynamically
    for col in gold_df.columns:
        gold_df[col] = gold_df[col].astype(str).str.strip()

    # Normalize Silver DataFrame dynamically
    for col in df_silver.columns:
        df_silver[col] = df_silver[col].astype(str).str.strip()

    # Rename Silver columns to Gold schema
    df_silver = df_silver.rename(columns=mapped_columns)

    # Add combined key for comparison
    df_silver["combined_key"] = df_silver[combined_key_columns].astype(str).agg("-".join, axis=1)
    gold_df["combined_key"] = gold_df[combined_key_columns].astype(str).agg("-".join, axis=1)

    # Identify new rows
    new_rows = df_silver[~df_silver["combined_key"].isin(gold_df["combined_key"])]

    # Drop combined key before returning new rows
    new_rows = new_rows.drop(columns=["combined_key"])
    columns_to_keep = []
    columns_to_keep = [col for col in new_rows.columns if col != None]
    new_rows = new_rows[columns_to_keep]

    # Normalize Silver DataFrame dynamically
    for col in new_rows.columns:
        if col is not None:
            new_rows[col] = new_rows[col].astype(str).str.strip()

    return new_rows


def get_modified_data_gold(df_silver, table_name, engine, column_name_mapping, fkey_mapping, table_relations):
    """
    Identify modified rows in Silver DataFrame compared to Gold DataFrame.

    Parameters:
        - df_silver (DataFrame): Silver DataFrame with potential updates.
        - table_name (str): Gold table name.
        - engine: SQLAlchemy engine for Gold schema.
        - column_name_mapping (dict): Mapping of column names from Silver to Gold schema.
        - fkey_mapping (dict): Foreign key mappings for Gold schema.
        - table_relations (dict): Contains old key columns mapping for Gold schema.

    Returns:
        - DataFrame: Modified rows to update in the Gold table.
    """
    # Map columns from Silver to Gold schema
    mapped_columns = column_name_mapping.get(table_name, {})
    if not mapped_columns:
        raise ValueError(f"No column mapping found for table {table_name}")

    # Extract old key columns and date column from table_relations
    old_key_columns = []
    date_column = None

    # Iterate through table_relations categories and tables
    for __, relations in table_relations.items():
        for relation in relations:
            if relation['tbl_gold'] == table_name:
                old_key_columns = relation.get('key_columns', [])
                date_column = relation.get('date_column', None)
                break  # Exit inner loop once the table is found
        if old_key_columns:  # Exit outer loop if the table is found
            break

    if not old_key_columns:
        raise ValueError(f"No key columns found for table {table_name} in table_relations")

    combined_key_columns = []
    gold_additional_columns = {}  # To store parent table key mapping for Gold

    for old_key in old_key_columns:
        if mapped_columns.get(old_key) is None:
            # If the key is mapped to None, use FK and parent table to fetch the old key
            fk_info = fkey_mapping.get(table_name, {}).get(old_key)
            if not fk_info:
                raise ValueError(f"No FK mapping found for key column '{old_key}' in table {table_name}")
            
            parent_tbl_gold, parent_pkey_column = fk_info
            fk_in_gold = next(
                (fk for fk, (parent_table, _) in fkey_mapping.get(table_name, {}).items() if parent_table == parent_tbl_gold),
                None
            )
            if not fk_in_gold:
                raise ValueError(f"No FK column found in {table_name} for parent table {parent_tbl_gold}")
            
            dp.logger.info(f"Fetching old key '{old_key}' using FK '{fk_in_gold}' -> '{parent_pkey_column}' from '{parent_tbl_gold}'")
            
            parent_query = f'SELECT "{parent_pkey_column}", "{old_key}" FROM "gold"."{parent_tbl_gold}"'
            parent_df = pd.read_sql(parent_query, con=engine)
            
            gold_additional_columns[old_key] = (fk_in_gold, parent_pkey_column, parent_df)
            combined_key_columns.append(old_key)
        else:
            # Otherwise, use the mapped column directly
            combined_key_columns.append(mapped_columns[old_key])

    if date_column:
        # Add the date column to the comparison keys if it exists
        mapped_date_column = mapped_columns.get(date_column)
        if mapped_date_column:
            combined_key_columns.append(mapped_date_column)
        else:
            dp.logger.warning(f"Date column '{date_column}' is not mapped for table '{table_name}'")

    if not combined_key_columns:
        raise ValueError(f"No valid key columns found for table {table_name}")

    # Build query to fetch Gold data
    query = (
        f"SELECT {', '.join([f'\"{col_gold}\"' for col_gold, __ in mapped_columns.items()])}"
        + f" FROM \"gold\".\"{table_name}\""
    )
    gold_df = pd.read_sql(query, con=engine)

    # Add old key columns from parent Gold tables to gold_df
    for old_key, (fk_in_gold, parent_pkey_column, parent_df) in gold_additional_columns.items():
        dp.logger.info(f"Adding old key '{old_key}' from parent table via '{fk_in_gold}'")
        gold_df = gold_df.merge(
            parent_df,
            how="left",
            left_on=fk_in_gold,
            right_on=parent_pkey_column,
            suffixes=("", f"_{old_key}")
        )
        gold_df.rename(columns={f"{old_key}_{old_key}": old_key}, inplace=True)

    # Normalize Gold DataFrame dynamically
    for col in gold_df.columns:
        if gold_df[col].dtype == 'object':  # Normalize string columns
            gold_df[col] = gold_df[col].astype(str).str.strip()

    # Normalize Silver DataFrame dynamically
    for col in df_silver.columns:
        if df_silver[col].dtype == 'object':  # Normalize string columns
            df_silver[col] = df_silver[col].astype(str).str.strip()

    # Rename Silver columns to Gold schema
    df_silver = df_silver.rename(columns=mapped_columns)

    # Add combined key for comparison
    df_silver["combined_key"] = df_silver[combined_key_columns].astype(str).agg("-".join, axis=1)
    gold_df["combined_key"] = gold_df[combined_key_columns].astype(str).agg("-".join, axis=1)

    # Merge to identify modified rows
    df_merged = df_silver.merge(gold_df, on="combined_key", how="left", suffixes=("", "_gold"))

    # Compare columns that are not combined_key or Gold-specific (_gold suffix)
    comparison_columns = [col for col in df_merged.columns if not col.endswith("_gold") and col != "combined_key"]

    # Identify rows with any differences
    df_modified = df_merged[
        df_merged[comparison_columns].ne(df_merged.filter(regex="_gold$").rename(lambda x: x[:-5], axis=1)).any(axis=1)
    ]

    # Drop combined_key and Gold-specific columns before returning
    if not df_modified.empty:
        df_modified = df_modified.drop(columns=["combined_key"] + df_merged.filter(regex="_gold$").columns)


    return df_modified




def update_modified_data_gold(df_mod_data, key_columns, db_tbl_name, column_name_mapping, conn):
    """
    Updates rows in a database table based on modified data provided in a Pandas DataFrame.

    Parameters:
        - df_mod_data (DataFrame): DataFrame with rows of data that has been modified.
        - key_columns (list of str): List of column names used to uniquely identify rows in the database.
        - db_tbl_name (str): Name of the database table to be updated.
        - column_name_mapping (dict): Mapping of column names from the Silver schema to the Gold schema.
        - conn (sqlalchemy.engine.base.Connection): Database connection.
    """
    if df_mod_data.empty:
        print(f"No modified data to update in table '{db_tbl_name}'.")
        return

    # Map the columns using the column_name_mapping for the specific table
    mapped_columns = column_name_mapping.get(db_tbl_name, {})
    if not mapped_columns:
        print(f"No column mapping found for table '{db_tbl_name}'. Skipping...")
        return

    print(f"Mapped columns for '{db_tbl_name}': {mapped_columns}")

    mapped_key_columns = [
        mapped_columns.get(key, key)
        for key in key_columns
        if mapped_columns.get(key, None) is not None
    ]

    for idx, fila in df_mod_data.iterrows():
        print(f"Processing row {idx}: {fila.to_dict()}")

        # Extract modified values for SET clause
        valores = {
            mapped_columns.get(col, col): fila[col]
            for col in df_mod_data.columns
            if mapped_columns.get(col, None) is not None
        }

        # Debugging output for values
        print(f"Values for SET clause: {valores}")

        if not valores:
            print(f"No values to update for row {idx}. Skipping...")
            continue

        # Generate SET and WHERE clauses
        set_clause = ', '.join([f'"{col}" = :{col}' for col in valores.keys()])
        where_clause = " AND ".join([
            f'"{mapped_columns.get(key, key)}" = :key_{key}'
            for key, mapped_key in zip(key_columns,mapped_key_columns)
        ])
        query = f'UPDATE "gold"."{db_tbl_name}" SET {set_clause} WHERE {where_clause}'

        # Create query parameters
        params = valores.copy()
        params.update({
            f'key_{key}': fila[key]
            for key in key_columns if key in fila
        })

        # Debugging output for query and parameters
        print(f"Generated Query: {query}")
        print(f"Query Parameters: {params}")

        # Execute the query
        try:
            with conn as conn:
                conn.execute(text(query), params)
                conn.commit()
        except Exception as e:
            print(f"Error updating modified data in table '{db_tbl_name}': {e}")


