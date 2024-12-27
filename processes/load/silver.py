import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import dependencies as dp
from processes.transform.silver import bronze_df
from processes.extract.silver import dataframes as silver_df
from db.engines import engine_silver, conn_silver
from model.table_relations import related_bron_silv
from processes.load.functions import get_new_data, upload_new_data, get_modified_data, update_modified_data

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
        df_new_data = get_new_data (
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

# Close connection
if conn_silver:
    conn_silver.close()

# print(':D')