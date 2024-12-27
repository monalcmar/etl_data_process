import os
import sys
from sqlalchemy.ext.automap import automap_base

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import dependencies as dp
from db.engines import engine_bronze, conn_bronze, engine_silver, conn_silver
from model.table_relations import related_bron_silv
from processes.extract.functions import map_db_tables, db_tables_to_df
from tasks.extraction import db_empty_tables, db_tables_to_df_resent
from model.table_relations import column_mappings
from processes.transform.functions import check_nulls, check_data_types
from processes.extract.silver import dataframes as silver_df
from model.table_relations import related_orig_bron
from processes.load.functions import get_new_data, upload_new_data, get_modified_data, update_modified_data


# # Get schema name acording to layer name
db_schema = os.path.splitext(os.path.basename(__file__))[0]


check_db_empty_tables = db_empty_tables(
    conn=conn_bronze,
    tbl_names_list=related_bron_silv,
    schema=db_schema
)

if check_db_empty_tables:
    dp.logger.info(f'All tables in Data Base "{db_schema}" Schema are empty, starting initial load')

# == Extract ==
    try:
        db_tables = map_db_tables(engine=engine_bronze, schema='bronze')
        bronze_df = db_tables_to_df(engine=engine_bronze, tables=db_tables)
        dp.logger.info(f"Extract Historic Data Process executed successfully in bronze schema.")

    except Exception as e:
        dp.logger.error(f"Extract Historic Data Proccess failed in bronze schema.: {e}")

        # dp.logger.info(f"Historical data has been loaded correctly in {db_schema} Schema.")

else:
    dp.logger.info(f"Historical data was already loaded in schema: bronze")

    try:
        bronze_df = db_tables_to_df_resent(
            engine=engine_bronze,
            tables=related_orig_bron
        )
        dp.logger.info(f"Extract Data Process executed successfully in bronze schema.")

    except Exception as e:
        dp.logger.error(f"Extract Data Proccess failed in bronze schema.: {e}")

        


# == Transform ==

# Asignar nuevos nombres a las columnas
for key, column_info in column_mappings.items():
    if key in bronze_df:
        try:
            # Validar el número de columnas
            if len(bronze_df[key].columns) != len(column_info):
                dp.logger.error(f"Column count mismatch for '{key}'. "
                            f"Expected: {len(column_info)}, Found: {len(bronze_df[key].columns)}.")
                continue
            
            bronze_df[key].columns = column_info.keys()
            dp.logger.info(f"Column names successfully updated for '{key}'.")

        except Exception as e:
            # Capturar y registrar cualquier otro error inesperado
            dp.logger.error(f"An error occurred while processing column names '{key}': {e}")
    else:
        dp.logger.error(f"Key '{key}' not found in bronze_df.")

# Check nulls and datatypes

for key, column_info in column_mappings.items():

    # Business rules apaño

    if key in {'U551_Presencia', 'U532_Trabajadas'}:
        bronze_df[key].drop(
            bronze_df[key][bronze_df[key]['NombreOperario'] == 'PRUEBA QUITER'].index,
            inplace=True
        )

    bronze_df[key], df_null_rows = check_nulls(bronze_df[key], column_info)

    bronze_df[key], df_invalid = check_data_types(bronze_df[key], column_info, df_null_rows)

# ===== Upload New Data =====

for key in related_bron_silv.keys():
    #if key in {'master_table', 'master_table_mult', 'fact_table', 'fact_table_mult'}:
    for table in related_bron_silv[key]:
        dp.logger.info(f'Processing updloading data process for table: "{table['tbl_silv']}"')
        # Accede a los valores del diccionario interno
        df = bronze_df[table['tbl_bron']]
        table_name = table['tbl_silv']
        key_columns = table['key_columns']
        date_column = table['date_column']

        # Execute upload new data function
        df_new_data, df_existing_data = get_new_data (
            df=df, 
            table_name=table_name,
            key_columns=key_columns,
            date_column=date_column,
            engine=engine_silver) 
            
        if not df_new_data.empty:
            dp.logger.info(f'There is new data to upload in table "{table_name}"')
            try:
                upload_new_data(
                    df_new_data=df_new_data,
                    table_name=table_name, 
                    date_column=date_column, 
                    engine=engine_silver)
                
                dp.logger.info(f'New data has been uploaded succesfully into table "{table_name}"')

            except Exception as e:
                dp.logger.error(f"An error has occurred trying to insert new data into table '{table_name}': {e}")
                continue
            
        else:
            dp.logger.info(f'There is not update data to insert into table "{table_name}"')


# ===== Update Modified Data =====

for key in related_bron_silv.keys():
    #if key in {'master_table', 'master_table_mult', 'fact_table', 'fact_table_mult'}:
    for table in related_bron_silv[key]:
        dp.logger.info(f'Processing updating data process fot table: "{table['tbl_silv']}"')
        # Accede a los valores del diccionario interno
        tbl_bron = table['tbl_bron']
        tbl_silv = table['tbl_silv']
        key_columns = table['key_columns']
        date_column = table['date_column']
        
        # Llama a la función usando los valores extraídos
        df_mod_data = get_modified_data(
            df_new_data=bronze_df[tbl_bron], 
            df_ref_data=silver_df[tbl_silv], 
            key_columns=key_columns,
            date_column=date_column
        )
        
        # Llamar a la función de modificacíón si hay datos para modificar
        if not df_mod_data.empty:
            dp.logger.info(f'There is data to update in table "{tbl_silv}"')
        
            try:                
                update_modified_data (
                    df_mod_data=df_mod_data,
                    key_columns=key_columns,
                    db_tbl_name=tbl_silv,
                    conn=conn_silver)
                
                dp.logger.info(f'Update data has been insert succesfully into table "{tbl_silv}": {e}')

            except Exception as e:
                dp.logger.error(f"An error has occurred trying to insert update data into table '{tbl_silv}': {e}")
                continue
        
        else:
            dp.logger.info(f'There is not update data to insert into table "{tbl_silv}"')



# Remember to close the connection when done
if conn_silver:
    conn_silver.close()


print(":D")