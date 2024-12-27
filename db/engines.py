import os 
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.connection import engine_setting, engine_connection

# Define database type and port for all schemas
db_type = 'postgresql' 
port = 5432

# == Silver Schema ==

# Get schema name acording to layer name
db_schema_bronze = 'bronze'

# Create engine for the specific schema
engine_bronze = engine_setting(db_type=db_type, db_port=port, db_schema=db_schema_bronze)

# Establish the connection
conn_bronze = engine_connection(engine_bronze, db_schema_bronze)

# == Silver Schema ==

# Get schema name acording to layer name
db_schema_silver = 'silver'

# Create engine for the specific schema
engine_silver = engine_setting(db_type=db_type, db_port=port, db_schema=db_schema_silver)

# Establish the connection
conn_silver = engine_connection(engine_silver, db_schema_silver)

# == Gold Schema ==

# Get schema name acording to layer name
db_schema_gold = 'gold'

# Create engine for the specific schema
engine_gold = engine_setting(db_type=db_type, db_port=port, db_schema=db_schema_gold)

# Establish the connection
conn_gold = engine_connection(engine_gold, db_schema_gold)