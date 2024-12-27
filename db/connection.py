import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import MetaData

# Add project path sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dependencies as dp
from config.config import db_host, db_name, db_password, db_user



def engine_create(db_type, db_name, user, password, host, port, schema=None, setinputsizes=True):
    '''
    Creates and returns a SQLAlchemy engine for the specified database type.

        input:
        - db_type (str): Type of database ('postgresql', 'mssql', or 'oracle').
        - db_name (str): Database name.
        - user (str): Username.
        - password (str): Password.
        - host (str): Database host.
        - port (int): Database port.
        - schema (str, optional): Schema name for PostgreSQL.
        - setinputsizes (bool, optional): Enables 'setinputsizes' for MSSQL (default: True).

        output:
        - SQLAlchemy Engine: Configured engine for the specified database.
    '''
    if db_type == 'postgresql':
        # Creates a dictionary for connect_args
        connect_args = {}
        if schema is not None:
            connect_args = {'options': f'-csearch_path={schema}'}

        engine = create_engine(
            f'postgresql://{user}:{password}@{host}:{port}/{db_name}', connect_args=connect_args
        )
    elif db_type == 'mssql':
        engine = create_engine(
            f'mssql+pyodbc://{user}:{password}@{host}/{db_name}'
            f'?driver=SQL+Server', use_setinputsizes=setinputsizes  #
        )
    elif db_type == 'oracle':
        engine = create_engine(
            f'oracle://{user}:{password}@{host}:{port}/{db_name}'
        )
    else:
        raise Exception('Database type not supported')

    return engine

def engine_setting (db_type, db_port, db_schema):
    '''
    Create and return a SQLAlchemy engine for a specified database schema.

    input: 
        - dt_type (str): database type.
        - db_port (str): database connection port.
        - db_schema (str): dtaba schema name.
    
    output: 
        - engine
    '''
    # Create engine for bronze schema
    engine = engine_create(
        db_type=db_type,
        db_name=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        schema= db_schema,
        setinputsizes=False
    )
    return engine

def engine_connection(engine, schema):
    '''
    Establish and return a connection to the given SQLAlchemy engine.

    input:
        - engine: engine
    output:
        - conn: connection to database. 
    '''
    try:
        conn = engine.connect()
        dp.logger.info(f"Successful connection to schema {schema}")
        return conn
    except Exception as e:
        dp.logger.error(f"Connection error in schema {schema}: {e}")
        return None


