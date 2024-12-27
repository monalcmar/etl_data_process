from datetime import date, timedelta

def empty_to_none () :
    '''Pending ...'''

def create_combined_key (df, key_columns, date_column=None):
    '''
    Creates a unique key from different key columns given.

    input:
        - df (DataFrame): Dataframe from which key_columns are taken.
        - key_columns (list): List of strings of the key columns names.
        - date_column str: Name of a column of date type (optional).

    output:
        - combined_key (Series): Serie of the combined key created from key_columns and date_column.

    '''
    combined_key = df[key_columns[0]].astype(str)

    for key in key_columns[1:]:
        combined_key += '_' + df[key].astype(str)

    if date_column:
        combined_key += '_' + df[date_column].astype(str)

    return combined_key

def build_upload_query(table_name, key_columns, date_column=None):
    """
    Constructs a SQL dynamic query based on the key_columns and date_column given.

    input:
        - table_name (str): Name o the table in database.
        - key_columns (str): List of strings of the key columns names.
        - date_column str: Name of a column of date type (optional).
        
    output:
        - query (str): SQL query as string. 
    """
    # Unir los nombres de las columnas clave
    selected_columns = ", ".join(f'"{col}"' for col in key_columns)

    # Iniciar la consulta base
    query = f'SELECT {selected_columns}'
    
    # Agregar columna de fecha si existe
    if date_column:
        query += f', "{date_column}"'

        # get date range
        current_date = date.today()
        min_date = current_date - timedelta(days=730)
        
        current_date = current_date.strftime('%Y-%m-%d')
        min_date = min_date.strftime('%Y-%m-%d')

    query += f' FROM "{table_name}"'

    # Agregar condiciones de fecha si se proporcionan
    if date_column and min_date and current_date:
        query += f' WHERE "{date_column}" BETWEEN \'{min_date}\' AND \'{current_date}\''

    return query


def build_update_query(table_name, key_columns, date_column=None):
    ''''''


def apply_ffill_invertidas (df_invertidas):
    '''Pending ...'''

        # Identificar las columnas que no sean 'Tiempo asig', 'Operario', 'T.INVERT.'
    columnas_sin_pilares = [col for col in df_invertidas.columns if col not in ['Tiempo asig', 'Operario', 'T.INVERT.']]

    # Crear la máscara:
    mascara2 = (
        df_invertidas[['Tiempo asig', 'Operario', 'T.INVERT.']].notnull().all(axis=1) &
        df_invertidas[columnas_sin_pilares].isnull().all(axis=1)
    )

    # Seleccionar las filas que cumplen la condición
    filas_a_rellenar = df_invertidas[mascara2]
    #print(filas_a_rellenar)

    # Aplicar forward fill en las filas seleccionadas para las columnas relevantes
    for col in columnas_sin_pilares:
        df_invertidas.loc[mascara2, col] = df_invertidas[col].ffill()


#-------------------------------------------------------------
# #CAMBIOS PARA TALLER ORDEN REPARACION

# # Filtrar las filas donde 'MO.SUB' no sea nulo pero el resto de las columnas sean nulas
# columnas_sin_mosub = [col for col in df_taller_orden_rep.columns if col != 'MO.SUB']
# mascara = df_taller_orden_rep['MO.SUB'].notnull() & df_taller_orden_rep[columnas_sin_mosub].isnull().all(axis=1)

# # Identificar las filas a modificar
# filas_a_rellenar = df_taller_orden_rep[mascara]
# ##print(filas_a_rellenar)

# # Aplicar forward fill en las filas seleccionadas para las columnas relevantes
# for col in columnas_sin_mosub:
#     df_taller_orden_rep.loc[mascara, col] = df_taller_orden_rep[col].ffill()

# # Guardar los cambios en el archivo Excel
# df_taller_orden_rep.to_excel(excel_path_2_taller_orden_rep, index=False)

# #comprob en la fila 86 se ha modificado bien
# #df_taller_orden_rep.iloc[1180:1190]
