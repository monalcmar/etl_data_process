import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from model.table_relations import column_mappings
#from processes.extract.bronze import dataframes as bronze_df
from processes.transform.functions import check_nulls, check_data_types

from src.silver import bronze_df

import dependencies as dp

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
            dp.logger.info(f"Columns successfully updated for '{key}'.")

        except Exception as e:
            # Capturar y registrar cualquier otro error inesperado
            dp.logger.error(f"An error occurred while processing '{key}': {e}")
    else:
        dp.logger.error(f"Key '{key}' not found in bronze_df.")

# Check nulls and datatypes

for key, column_info in column_mappings.items():

    bronze_df[key], df_null_rows = check_nulls(bronze_df[key], column_info)

    bronze_df[key], df_invalid = check_data_types(bronze_df[key], column_info, df_null_rows)

    #bronze_df[key] = bronze_df[key].iloc[:, :-2]

# print(':D')



