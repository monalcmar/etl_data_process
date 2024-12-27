import os
import sys
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import dependencies as dp
# from logger.logger import logger

# logger = logger()

def map_db_tables (engine, schema):
    """
    Mapea las tablas de una base de datos en un esquema especificado.

    Args:
        engine: SQLAlchemy engine conectado a la base de datos.
        schema: Nombre del esquema en la base de datos.

    Returns:
        dict: Diccionario donde las claves son nombres de tablas y los valores son objetos Table.
    """
    try:
        dp.logger.info(f"Mapping database tables in schema '{schema}' started.")

        metadata = MetaData()

        metadata.reflect(bind=engine, schema=schema)
        
        Base = automap_base(metadata=metadata)
        Base.prepare()

        tables = {}

        for table_name in metadata.tables:
            tables[table_name] = Table(table_name, metadata, autoload_with=engine)

        dp.logger.info(f"Tables in schema '{schema}' were successfully mapped.")

        return tables
    
    except SQLAlchemyError as e:
        dp.logger.error(f"Error mapping tables in schema '{schema}': {e}")
        raise

def db_tables_to_df (engine, tables):
    """
    Carga los datos de un conjunto de tablas en DataFrames.

    Args:
        engine: SQLAlchemy engine conectado a la base de datos.
        tables: Dict con nombres de tablas y sus objetos Table.

    Returns:
        dict: Diccionario con nombres de tablas como claves y DataFrames como valores.
    """
    try:
        
        dataframes = {}

        for table_name, table_obj in tables.items():
            dp.logger.info(f'Loading data from {table_name} table...')
            table_name = table_name.split('.')[-1]

            query = f'SELECT * FROM "{table_name}"'
            dataframes[table_name] = pd.read_sql(query, con=engine).iloc[:, :-2]

            dp.logger.debug(f'Data from {table_name} table has been load in a DataFrame.')

    except Exception as e:
        dp.logger.error(f"Error loading data from table '{table_name}': {e}")
        raise
    
    dp.logger.info("Data from all tables has been successfully loaded into DataFrames.")

    return dataframes

