import os
import sys
from sqlalchemy.ext.automap import automap_base

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dependencies as dp
from db.engines import engine_bronze, conn_bronze, engine_silver, conn_silver

dp.set_logger(schema=db_schema, process="Extract", task="Incremental Extractio")