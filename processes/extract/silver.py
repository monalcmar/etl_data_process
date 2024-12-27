import os
import sys
from sqlalchemy.ext.automap import automap_base

#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from db.engines import engine_silver, conn_silver
from processes.extract.functions import map_db_tables, db_tables_to_df
# from logger.logger import logger
import dependencies as dp

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

#logger = logger()

# # Get schema name acording to layer name
db_schema = os.path.splitext(os.path.basename(__file__))[0]

# == Extract ==
try:
    db_tables = map_db_tables(engine=engine_silver, schema=db_schema)
    dataframes = db_tables_to_df(engine=engine_silver, tables=db_tables)
    dp.logger.info(f"Extract Process executed successfully in {db_schema} schema.")

except Exception as e:
    dp.logger.error(f"Extract Proccess failed in {db_schema} schema.: {e}")


# Remember to close the connection when done
if conn_silver:
    conn_silver.close()

# print(':D')