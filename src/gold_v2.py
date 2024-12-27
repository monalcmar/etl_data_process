import os
import sys
import pandas as pd
import numpy as np
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from pathlib import Path
from datetime import date, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dependencies as dp
from db.engines import engine_silver, conn_silver, engine_gold, conn_gold
from processes.extract.functions import map_db_tables, db_tables_to_df
from processes.transform.functions import check_nulls, check_data_types
from processes.load.functions import get_new_data, upload_new_data, get_modified_data, update_modified_data
from tasks.extraction import db_empty_tables
from model.gold_schema_mappings import pkey_mapping, fkey_mapping, column_name_mapping
from model.table_relations import related_silv_gold, related_silv_gold_v2
from processes.transform.functions import assing_foreig_keys
from model.model_info import gold_properties


# === Define schema and connection ===
db_schema = os.path.splitext(os.path.basename(__file__))[0]
conn = conn_gold

# # === Check for empty Gold tables ===
# check_db_empty_tables = db_empty_tables(
#     conn=conn_gold, tbl_names_list=related_silv_gold, schema=db_schema
# )

# if check_db_empty_tables:
#     dp.logger.info(
#         f'All tables in Gold schema "{db_schema}" are empty, starting initial load.'
#     )

# extract data from silver 
try:
    db_tables = map_db_tables(engine=engine_silver, schema='silver')
    silver_df = db_tables_to_df(engine=engine_silver, tables=db_tables)
    dp.logger.info(f"Extract Historic Data Process executed successfully in silver schema.")

except Exception as e:
    dp.logger.error(f"Extract Historic Data Proccess failed in bronze schema.: {e}")


# # === Extract Silver Tables ===
# try:
#     db_tables = map_db_tables(engine=engine_silver, schema="silver")
#     silver_df = db_tables_to_df(engine=engine_silver, tables=db_tables)
#     dp.logger.info(f"Silver schema data successfully extracted.")
# except Exception as e:
#     dp.logger.error(f"Error extracting Silver schema data: {e}")
#     conn.close()
#     sys.exit(1)


# Ordered tables to follow constraints

ordered_tables = [
    "TiposOrdenesReparacion",
    "TiposVentasAlmacen",
    # "Articulos",
    "TiposHoras",
    "Clientes",
    "Empresas",
    "Vehiculos",
    "Talleres",
    "Operarios",
    "Almacenes",
    #"Stock",
    "BonosPresencia",
    "OrdenesReparacion",
    "BonosTrabajadas",
    # "Compras",
    "Invertidas",
    # "OrdenesVentaMostrador",
    # "OrdenesVentaTaller"
]

# === Process and Load Data ===

df_silver_fkeys = {}

for tbl_gold in ordered_tables:
    dp.logger.info(f"Processing table: Silver '{tbl_gold}' -> Gold '{tbl_gold}'")

    if tbl_gold in fkey_mapping.keys():
        dp.logger.debug(f'Table {tbl_gold} needs to assign foreign keys.')
        
        # Get relations of Foreign Keys 
        fk_relations = fkey_mapping[tbl_gold]
        dp.logger.debug(f"FK Processing table: {tbl_gold}")

        df_silver_fkeys[tbl_gold] = assing_foreig_keys (
            tbl_gold,
            silver_df[tbl_gold],
            fkey_mapping[tbl_gold],
            conn
        )

    else:
        df_silver_fkeys[tbl_gold] = silver_df[tbl_gold]

    dp.logger.debug(f"Applying transforme functions to '{tbl_gold}'")

    df_silver_fkeys[tbl_gold], df_null_rows = check_nulls(df_silver_fkeys[tbl_gold], gold_properties[tbl_gold])

    df_silver_fkeys[tbl_gold], df_invalid = check_data_types(df_silver_fkeys[tbl_gold], gold_properties[tbl_gold], df_null_rows)

    table_relations = related_silv_gold_v2[tbl_gold]
    for relation in table_relations:
        tbl_silv = relation.get("tbl_gold") ## OJO relation.get("tbl_silv")
        df = df_silver_fkeys[tbl_gold] ### OJO  ## silver_df[tbl_gold] 
        table_name = tbl_gold
        key_columns = relation.get("key_columns")
        date_column = relation.get("date_column")


    df_new_data, df_existing_data = get_new_data (
        df=df, 
        table_name=table_name,
        key_columns=key_columns,
        date_column=date_column,
        engine=engine_gold)
    
    if not df_new_data.empty:
        dp.logger.info(f'There is new data to upload in table "{table_name}"')

        dp.logger.info(f"Assigning new IDs for table '{tbl_gold}'")
        pkey_column = pkey_mapping.get(tbl_gold)

        result = conn.execute(
            text(f'SELECT MAX("{pkey_column}") FROM "gold"."{tbl_gold}"')
        )

        max_existing_id = result.scalar() or 0

        df_new_data[pkey_column] = range( # silver_df
            max_existing_id + 1, max_existing_id + 1 + len(df_new_data)
        )

        try:
            upload_new_data(
                df_new_data=df_new_data,
                table_name=table_name, 
                date_column=date_column, 
                engine=engine_gold)
            
            dp.logger.info(f'New data has been uploaded succesfully into table "{tbl_gold}"')

        except Exception as e:
            dp.logger.error(f"An error has occurred trying to insert new data into table '{tbl_gold}': {e}")
            continue
            
    else:
        dp.logger.info(f'There is not update data to insert into table "{table_name}"')


        # # Check for modified data and update
        # df_modified_data = get_modified_data_gold(
        #     df_silver=df_silver,
        #     table_name=tbl_gold,
        #     engine=engine_gold,
        #     column_name_mapping=column_name_mapping,
        #     fkey_mapping=fkey_mapping,
        #     table_relations=related_silv_gold,
        # )

        # if not df_modified_data.empty:
        #     dp.logger.info(
        #         f"Modified data found for Gold table '{tbl_gold}'. Updating..."
        #     )
        #     try:
        #         update_modified_data_gold(
        #             df_mod_data=df_modified_data,
        #             key_columns=key_columns,
        #             db_tbl_name=tbl_gold,
        #             column_name_mapping=column_name_mapping,
        #             conn=conn,
        #         )
        #         dp.logger.info(
        #             f"Modified data successfully updated in table '{tbl_gold}'."
        #         )
        #     except Exception as e:
        #         dp.logger.error(
        #             f"Error updating modified data in table '{tbl_gold}': {e}"
        #         )
        # else:
        #     dp.logger.info(f"No modified data found in table '{tbl_gold}'.")

# Close the connection
if conn:
    conn.close()

dp.logger.info("Gold processing completed.")
print(":D")
