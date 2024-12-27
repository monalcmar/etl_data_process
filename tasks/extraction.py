import os
import sys
from sqlalchemy import MetaData, Table, text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from datetime import date, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import dependencies as dp
from datetime import date, timedelta

def db_empty_tables (conn, tbl_names_list, schema):
    ''''''
    empty_tables = {}
    if schema == "silver":
        tbl = 'tbl_silv'
    elif schema == "gold":
        tbl = 'tbl_gold'
    for key in tbl_names_list.keys():
        for table in tbl_names_list[key]:
            dp.logger.info(f'Transforming data for DataFrame: "{table[tbl]}"')
            table_name = table[tbl]

            exists_query = text("""
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_schema = :schema AND table_name = :table_name
            )
        """)
        exists = conn.execute(exists_query, {"schema": schema, "table_name": table_name}).scalar()

        if exists:
            count_query = text(f'SELECT COUNT(*) FROM "{schema}"."{table_name}"')
            count = conn.execute(count_query).scalar()
            empty_tables[table_name] = count == 0
        else:
            empty_tables[table_name] = None

    return all(is_empty for is_empty in empty_tables.values())


def db_tables_to_df_resent (engine, tables):
    ''''''
    dataframes = {}

    for key in tables.keys():
        #if key in {'master_table', 'master_table_mult', 'fact_table', 'fact_table_mult'}:
        for table in tables[key]:
            table_name = table['tbl_bron']
            date_column = table['date_column']

            try:
                if date_column:
                    # get date range
                    current_date = date.today()
                    min_date = current_date - timedelta(days=730)

                    current_date = current_date.strftime('%Y-%m-%d')
                    min_date = min_date.strftime('%Y-%m-%d')

                    query = f'SELECT * FROM "{table_name}" WHERE "{date_column}" BETWEEN \'{min_date}\' AND \'{current_date}\''

                else:
                    query = f'SELECT * FROM "{table_name}"'


                dataframes[table_name] = pd.read_sql(query, con=engine).iloc[:, :-2]

                dp.logger.info(f'Data from {table_name} table has been load in a DataFrame.')

            except Exception as e:
                dp.logger.error(f"Error loading data from table '{table_name}': {e}")
                raise
    
    return dataframes