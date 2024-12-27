import os
import sys
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dependencies as dp
from db.engines import engine_silver, conn_silver, engine_gold, conn_gold
from model.table_relations import related_silv_gold
from tasks.extraction import db_empty_tables
from processes.extract.functions import map_db_tables, db_tables_to_df
from processes.load.functions import (
    get_new_data_gold, get_new_data,
    update_modified_data_gold,
    upload_new_data,
    get_modified_data_gold,
    get_modified_data, update_modified_data
)
from model.gold_schema_mappings import (
    pkey_mapping,
    fkey_mapping,
    column_name_mapping,
    fk_column_silver_mapping
)
from model.table_relations import related_silv_gold_v2

# === Define schema and connection ===
db_schema = os.path.splitext(os.path.basename(__file__))[0]
conn = conn_gold

# === Check for empty Gold tables ===
check_db_empty_tables = db_empty_tables(
    conn=conn_gold, tbl_names_list=related_silv_gold, schema=db_schema
)

if check_db_empty_tables:
    dp.logger.info(
        f'All tables in Gold schema "{db_schema}" are empty, starting initial load.'
    )

# === Extract Silver Tables ===
try:
    db_tables = map_db_tables(engine=engine_silver, schema="silver")
    silver_df = db_tables_to_df(engine=engine_silver, tables=db_tables)
    dp.logger.info(f"Silver schema data successfully extracted.")
except Exception as e:
    dp.logger.error(f"Error extracting Silver schema data: {e}")
    conn.close()
    sys.exit(1)

# Ordered tables to follow constraints

ordered_tables = [
    #"TiposOrdenesReparacion",
    #"TiposVentasAlmacen",
    #"Articulos",
    #"TiposHoras",
    #"Clientes",
    #"Empresas",
    "Vehiculos",
    "Talleres",
    "Operarios",
    "Almacenes",
    "Stock",
    "BonosPresencia",
    "OrdenesReparacion",
    "BonosTrabajadas",
    "Compras",
    "Invertidas",
    "OrdenesVentaMostrador",
    "OrdenesVentaTaller",
]

# === Get existing Gold Data ===

# === Extract Gold Tables ===
# try:
#     db_tables = map_db_tables(engine=engine_gold, schema="gold")
#     existing_gold_df = db_tables_to_df(engine=engine_gold, tables=db_tables)
#     dp.logger.info(f"Silver schema data successfully extracted.")
# except Exception as e:
#     dp.logger.error(f"Error extracting Gold schema data: {e}")
#     conn.close()
#     sys.exit(1)

# === Process and Load Data ===
for tbl_gold in ordered_tables:
    table_relations = [
        rel
        for rel in related_silv_gold.get("master_table", [])
        + related_silv_gold.get("master_table_mult", [])
        + related_silv_gold.get("fact_table", [])
        + related_silv_gold.get("fact_table_mult", [])
        if rel["tbl_gold"] == tbl_gold
    ]
    for relation in table_relations:
        tbl_silv = relation["tbl_silv"]
        key_columns = relation["key_columns"]
        date_column = relation["date_column"]

        # Get PKey from schema mapping
        pkey_column = pkey_mapping.get(tbl_gold)
        if not pkey_column:
            dp.logger.error(f"No PKey mapping found for table '{tbl_gold}'")
            continue

        dp.logger.info(f"Processing table: Silver '{tbl_silv}' -> Gold '{tbl_gold}'")

        # Load Silver DataFrame
        df_silver = silver_df[tbl_silv]

        # Check for new data in Gold
        df_new_data = get_new_data_gold(
                        df_silver=df_silver,
                        table_name=tbl_gold,
                        engine=engine_gold,
                        column_name_mapping=column_name_mapping,
                        fkey_mapping=fkey_mapping,
                        table_relations=related_silv_gold
                    )

        # Insert new data
        if not df_new_data.empty:
            dp.logger.info(f"New data found for Gold table '{tbl_gold}'.")

            
            # Foreign Key Handling
            if tbl_gold in fkey_mapping:
                # Iterate over each foreign key relationship for the current table
                for fk_column, (parent_tbl_gold, parent_pkey_columns) in fkey_mapping[tbl_gold].items():
                    # Ensure parent_pkey_columns is a list for consistency
                    if isinstance(parent_pkey_columns, str):
                        parent_pkey_columns = [parent_pkey_columns]

                    # Determine corresponding Silver columns for each parent primary key column
                    silver_fk_column = [
                        fk_column_silver_mapping.get(tbl_gold, {})[fk_column]
                    ]

                    # Restore any required Silver columns temporarily
                    for col in silver_fk_column:
                        if col not in df_new_data.columns and col in df_silver.columns:
                            dp.logger.info(f"Restoring column '{col}' from Silver for FK processing in table '{tbl_gold}'.")
                            df_new_data[col] = df_silver[col]

                    # Fetch parent table data for the necessary columns
                    parent_columns_to_fetch = parent_pkey_columns + silver_fk_column
                    parent_query = f'SELECT "{'","'.join(parent_columns_to_fetch)}" FROM "gold"."{parent_tbl_gold}"'
                    parent_df_gold = pd.read_sql(parent_query, con=engine_gold)
                    parent_df_gold.drop_duplicates(subset=parent_pkey_columns, inplace=True)

                    # Normalize parent Gold DataFrame dynamically
                    for col in parent_df_gold.columns:
                        parent_df_gold[col] = parent_df_gold[col].astype(str).str.strip()

                    # Merge parent table data to resolve FK using composite keys
                    df_new_data = df_new_data.merge(
                        parent_df_gold,
                        how="left",
                        left_on=silver_fk_column,
                        right_on=parent_pkey_columns,
                        suffixes=("", "_parent"),
                    )

                    # Assign the foreign key value
                    df_new_data[fk_column] = df_new_data[parent_pkey_columns[0]]

                    # Drop the parent primary key columns if not part of the Gold schema
                    df_new_data.drop(columns=parent_pkey_columns, inplace=True, errors="ignore")

                    dp.logger.info(f"Foreign key '{fk_column}' mapped successfully using columns {silver_fk_column}.")


        else:
            dp.logger.info(f"No Foreign key found for table '{tbl_gold}'.")

        # Assign new IDs for new rows
        dp.logger.info(f"Assigning new IDs for table '{tbl_gold}'")
        result = conn.execute(
            text(f'SELECT MAX("{pkey_column}") FROM "gold"."{tbl_gold}"')
        )
        max_existing_id = result.scalar() or 0
        df_new_data[pkey_column] = range(
            max_existing_id + 1, max_existing_id + 1 + len(df_new_data)
        )

        # Apply column name mapping before inserting
        if tbl_gold in column_name_mapping:
            df_new_data.rename(columns=column_name_mapping[tbl_gold], inplace=True)

            final_columns = [pkey_mapping[tbl_gold]] + [
                col for col in column_name_mapping[tbl_gold].values() if col
            ]
            df_new_data = df_new_data[final_columns]

        # Insert new data
        try:
            upload_new_data(
                df_new_data=df_new_data,
                table_name=tbl_gold,
                engine=engine_gold,
                date_column=date_column,
            )
            dp.logger.info(f"New data successfully uploaded to table '{tbl_gold}'.")
        except Exception as e:
            dp.logger.error(f"Error uploading new data to table '{tbl_gold}': {e}")
    else:
        dp.logger.info(f"No new data found in table '{tbl_gold}'.")

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
