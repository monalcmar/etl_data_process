import os
import sys
from sqlalchemy.ext.automap import automap_base
import pandas as pd
from pathlib import Path
import warnings
from sqlalchemy.exc import SQLAlchemyError

warnings.simplefilter("ignore")

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dependencies as dp
from model.table_relations import related_orig_bron
from db.connection import engine_setting, engine_connection
from processes.transform.functions import all_columns_to_str
from processes.load.functions import upload_new_data_master, upload_new_data_fact, upload_new_data_fact_mult
from processes.load.functions import get_new_data, upload_new_data, get_modified_data, update_modified_data
# from db.engines import engine_bronze, conn_bronze
from processes.extract.bronze import dataframes as  bronze_df
from utils.functions import apply_ffill_invertidas
# from dp.logger.dp.logger import dp.logger
from processes.bronze.extract import list_files_in_most_recent_date, incremental_data, are_historical_tables_empty, historical_data, delete_old_data
from processes.bronze.extract import incrementales_contabilidad, historicos_taller, incrementales_taller, prefijos_bronze, prefijos_historicos
from db.engines import engine_bronze, conn_bronze

# dp.logger = dp.logger()

# = Connection to schema ddbb =

# Define database type and port
db_type = 'postgresql'
port = 5432

# Get schema name according to layer name
db_schema = os.path.splitext(os.path.basename(__file__))[0]
print(db_schema)

# Create engine for the specific schema
engine = engine_setting(db_type=db_type, db_port=port, db_schema=db_schema)

# Establish the connection
conn = engine_connection(engine, schema=db_schema)

# === Extract Data ===
rootFolder = Path(__file__).parent.parent

mas_recientes_contabilidad, ficheros = list_files_in_most_recent_date(incrementales_contabilidad)
mas_recientes_taller, ficheros = list_files_in_most_recent_date(incrementales_taller)

dp.logger.info(f"Los últimos datos de contabilidad son: {mas_recientes_contabilidad}")
dp.logger.info(f"Los últimos datos de taller son: {mas_recientes_taller}")

# === Delete Old Data === #

# If there were more than 20 directories with format: "ddmmyyyy" it would delete the oldest one

borrado_contabilidad = delete_old_data(incrementales_contabilidad)
borrado_taller = delete_old_data(incrementales_taller)

if borrado_contabilidad and borrado_taller:
    dp.logger.info("Se han borrado los directorios incrementales más antiguos de contabilidad y taller")
else:
    dp.logger.info("No se han borrado directorios incrementales.")


# === Extract Historical Data (Initial Load) ===

check_tablas_historicas_vacias = are_historical_tables_empty(conn, prefijos_historicos)

if check_tablas_historicas_vacias:
    dp.logger.info("All the historical tables are empty, starting initial load")

    try:
        # Create dfs
        #df_vehiculos_historico = historical_data(historicos_taller, prefijos_bronze["vehiculos"])
        df_presencia_historico = historical_data(historicos_taller, prefijos_bronze["bonos_presencia"])
        df_trabajadas_historico = historical_data(historicos_taller, prefijos_bronze["bonos_trabajadas"])
        df_compras_historico = historical_data(historicos_taller, prefijos_bronze["compras"])
        df_invertidas_historico = historical_data(historicos_taller, prefijos_bronze["invertidas"])
        df_ordenes_reparacion_historico = historical_data(historicos_taller, prefijos_bronze["ordenes_reparacion"])
        df_ventas_mostrador_historico = historical_data(historicos_taller, prefijos_bronze["ordenes_venta_mostrador"])
        df_ventas_taller_historico = historical_data(historicos_taller, prefijos_bronze["ordenes_venta_taller"])
        
        # Transform dfs
        #df_vehiculos_historico = all_columns_to_str(df_vehiculos_historico)
        df_presencia_historico = all_columns_to_str(df_presencia_historico)
        df_trabajadas_historico = all_columns_to_str(df_trabajadas_historico)
        df_compras_historico = all_columns_to_str(df_compras_historico)
        df_invertidas_historico = all_columns_to_str(df_invertidas_historico)
        df_ordenes_reparacion_historico = all_columns_to_str(df_ordenes_reparacion_historico)
        df_ventas_mostrador_historico = all_columns_to_str(df_ventas_mostrador_historico)
        df_ventas_taller_historico = all_columns_to_str(df_ventas_taller_historico)

        apply_ffill_invertidas(df_invertidas_historico)

        
        with engine.begin() as conn:
            #upload_new_data_master(df_vehiculos_historico, 'U6341303_Vehiculos', 'Bastidor', conn)
            upload_new_data_fact_mult(df_presencia_historico, 'U551_Presencia', ['Operario', 'ENTRADA PRES'], 'Fecha', conn)
            upload_new_data_fact_mult(df_trabajadas_historico, 'U532_Trabajadas', ['Operario', 'Entra'], 'Fecha', conn)
            upload_new_data_fact_mult(df_compras_historico, 'U553_Compras', ['Referenci', 'Artículo'], 'Fecha', conn)
            upload_new_data_fact_mult(df_invertidas_historico, 'U555_Invertidas', ['REF.OR', 'Operario'], 'Fec.apertu', conn)
            upload_new_data_fact(df_ordenes_reparacion_historico, 'U533_OrdenesReparacion', 'REF.OR', 'Fec.apertu', conn)
            upload_new_data_fact(df_ventas_mostrador_historico, 'U554_VentasMostrador', 'Refer.', 'Fecha', conn)
            upload_new_data_fact(df_ventas_taller_historico, 'U560_VentasTaller', 'Refer.', 'Fec.sali', conn)

        dp.logger.info("Historical data has been loaded correctly.")
    
    except SQLAlchemyError as e:
        dp.logger.error(f"Error loading historical data: {str(e)}")
else:
    dp.logger.info("Historical data was already loaded")



# === Extract Most Recent Data ===

# Contabilidad

df_cliente = incremental_data(incrementales_contabilidad, mas_recientes_contabilidad, prefijos_bronze["clientes"])
df_empresas = incremental_data(incrementales_contabilidad, mas_recientes_contabilidad, prefijos_bronze["empresas"])

# Taller

df_bonos_trab = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["bonos_trabajadas"])
df_taller_orden_rep = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["ordenes_reparacion"])
df_bono_pres = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["bonos_presencia"])
df_stock = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["stock"])
df_compras = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["compras"])
df_mostrador = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["ordenes_venta_mostrador"])
df_invertidas = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["invertidas"])
df_taller_orden_venta = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["ordenes_venta_taller"])
df_articulos = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["articulos"])
df_talleres = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["talleres"])
df_almacenes = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["almacenes"])
df_operarios = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["operarios"])
df_vehiculos = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["vehiculos"])
df_tipos_horas = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["tipos_horas"])
df_tipos_venta = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["tipos_ventas_almacen"])
df_tipos_ordenes = incremental_data(incrementales_taller, mas_recientes_taller, prefijos_bronze["tipos_ordenes_reparacion"])



# # === Transform Data ===

dp.logger.info(f'Transform process has started in {db_schema}')

for key in related_orig_bron.keys():
    for df_info in related_orig_bron[key]:
        dp.logger.debug(f'Transforming data for DataFrame: "{df_info['df_orig']}"')

        if df_info['df_orig'] == 'df_invertidas':

            try:
                apply_ffill_invertidas(df_invertidas)
                dp.logger.info(f'Apply forward fill to DataFrame: "{df_info['df_orig']}" succesfully.')

            except Exception as e:
                dp.logger.error(f'An error has occurred when applying ffill() to DataFrame: "{df_info['df_orig']}": {e}')
            
        try:
            globals()[df_info['df_orig']] = all_columns_to_str(globals()[df_info['df_orig']])
            dp.logger.info(f'Transforming data for DataFrame: "{df_info['df_orig']}" succesfully.')

        except Exception as e:
            dp.logger.error(f'An error has occurred when transforming data for DataFrame "df_invertidas": {e}')

            continue

dp.logger.info(f'Transform process has ended in {db_schema}')



# # === Load Data ===

dp.logger.debug(f'Load process has started in {db_schema}')

# = Upload data =
dp.logger.debug(f'Upload new data process has started in {db_schema}')

for key in related_orig_bron.keys():
    # if key in {'master_table', 'master_table_mult', 'fact_table', 'fact_table_mult'}:
    for table in related_orig_bron[key]:
        dp.logger.debug(f'Uploading new data for Table: "{table['tbl_bron']}"')

        # if table['tbl_bron'] == 'U555_Invertidas':

        # Get the info diccionary data
        df = globals()[table['df_orig']]
        table_name = table['tbl_bron']
        key_columns = table['key_columns']
        date_column = table['date_column']

        try:
            df_new_data, df_existing_data = get_new_data (
                df=df, 
                table_name=table_name,
                key_columns=key_columns,
                date_column=date_column,
                engine=engine_bronze)
            
            # print(':D')
                            
            if not df_new_data.empty:
                dp.logger.info(f'There is new data to upload in table "{table_name}"')
                try:
                    upload_new_data(
                        df_new_data=df_new_data,
                        table_name=table_name, 
                        date_column=date_column, 
                        engine=engine_bronze)
                    
                    dp.logger.info(f'New data has been uploaded succesfully into table "{table_name}"')

                except Exception as e:
                    dp.logger.error(f"An error has occurred trying to insert new data into table '{table_name}': {e}")
                    continue
                
            else:
                dp.logger.info(f'There is not update data to insert into table "{table_name}"')

        except Exception as e:
            dp.logger.error(f"An error has occurred trying to get new data from table '{table_name}': {e}")

            continue

dp.logger.debug(f'Upload new data process has ended in {db_schema}')

# = Update data =

dp.logger.debug(f'Update new data process has started in {db_schema}')

for key in related_orig_bron.keys():
    #if key in {'master_table', 'master_table_mult'}: #, 'fact_table', 'fact_table_mult'}:
    for table in related_orig_bron[key]:
        dp.logger.debug(f'Updating modified data for Table: "{table['tbl_bron']}"')

        # Get the info diccionary data
        tbl_orig = table['df_orig']
        tbl_bron = table['tbl_bron']
        key_columns = table['key_columns']
        date_column = table['date_column']

        try:
            df_mod_data = get_modified_data(
                df_new_data=globals()[tbl_orig], 
                df_ref_data=bronze_df[tbl_bron], 
                key_columns=key_columns,
                date_column=date_column
            )

            
            # Llamar a la función de modificacíón si hay datos para modificar
            if not df_mod_data.empty:
                dp.logger.info(f'There is data to update in table "{tbl_bron}"')
            
                try:
                    with conn_bronze.begin() as transaction:                
                        update_modified_data (
                            df_mod_data=df_mod_data,
                            key_columns=key_columns,
                            db_tbl_name=tbl_bron,
                            conn=conn_bronze)
                        
                    dp.logger.debug(f'Update data has been insert succesfully into table "{tbl_bron}": {e}')

                except Exception as e:
                    dp.logger.error(f"An error has occurred trying to insert update data into table '{tbl_bron}': {e}")
                    continue

            dp.logger.info(f'There is not data to update for table "{tbl_bron}"')

        except Exception as e:
            dp.logger.error(f"An error has occurred trying to get modified data from table '{table_name}': {e}")

            continue

dp.logger.debug(f'Update new data process has ended in {db_schema}')

# Close connection
if conn:
    conn.close()

dp.logger.debug(f'Load process has ended in {db_schema}')

print(':D')