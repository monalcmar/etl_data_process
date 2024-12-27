import os
import sys
from sqlalchemy.ext.automap import automap_base


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from db.engines import engine_bronze, conn_bronze
from processes.extract.functions import map_db_tables, db_tables_to_df
from tasks.extraction import db_tables_to_df_resent
from model.table_relations import related_orig_bron
import dependencies as dp


# Get schema name acording to layer name
db_schema = os.path.splitext(os.path.basename(__file__))[0]
tables = related_orig_bron

# == Extract Historic Data==
try:
    db_tables = map_db_tables(engine=engine_bronze, schema=db_schema)
    dataframes = db_tables_to_df(engine=engine_bronze, tables=db_tables)
    dp.logger.info(f"Extract Historic Data Process executed successfully in {db_schema} schema.")

except Exception as e:
    dp.logger.error(f"Extract Historic Data Proccess failed in {db_schema} schema.: {e}")



# # Remember to close the connection when done
# if conn_bronze:
#     conn_bronze.close()

print(':D')