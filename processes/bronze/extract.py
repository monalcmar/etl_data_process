from sqlalchemy import create_engine, text
from datetime import datetime
import pandas as pd
from pathlib import Path
import os
import shutil


# Ruta general de archivos historicos

historicos_taller = Path(r"C:\archivos_etl\destino_taller\historico")

# Ruta general de archivos incrementales

incrementales_contabilidad = Path(r"C:\archivos_etl\destino_Contabilidad")
incrementales_taller = Path(r"C:\archivos_etl\destino_taller/incremental")

# Prefijos de los archivos en bronze

prefijos_bronze = {
    'empresas': 'U6311303',
    'clientes': 'U6301303',
    'bonos_trabajadas': 'U532',
    'almacenes': 'U6321303',
    'articulos': 'U6301303',
    'operarios': 'U6331303',
    'talleres': 'U6311303',
    'tipos_horas': 'ULSTTHPT',
    'tipos_ordenes_reparacion': 'UU2',
    'tipos_ventas_almacen': 'ULSTTVPT',
    'vehiculos': 'U6341303',
    'bonos_presencia': 'U551',
    'compras': 'U553',
    'invertidas': 'U555',
    'stock': 'U552',
    'ordenes_reparacion': 'U533',
    'ordenes_venta_mostrador': 'U554',
    'ordenes_venta_taller': 'U560',
}

# prefijos historicos

prefijos_historicos = {
    "vehiculos": "U6341303_Vehiculos",
    "presencia": "U551_Presencia",
    "trabajadas": "U532_Trabajadas",
    "compras": "U553_Compras",
    "invertidas": "U555_Invertidas",
    "stock": "U552_Stock",
    "ordenes_reparacion": "U533_OrdenesReparacion",
    "ventas_mostrador": "U554_VentasMostrador",
    "ventas_taller": "U560_VentasTaller"
}



# devuelve una lista con las tablas que están vacias
def check_empty_tables(engine, schema="bronze"):
    empty_tables = {}
    query = text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = :schema
    """)
    
    with engine.connect() as conn:
        result = conn.execute(query, {"schema": schema}).fetchall()
        tables = [row[0] for row in result]

        for table in tables:
            exists_query = text("""
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_schema = :schema AND table_name = :table
                )
            """)
            exists = conn.execute(exists_query, {"schema": schema, "table": table}).scalar()
            if exists:
                count_query = text(f'SELECT COUNT(*) FROM "{schema}"."{table}"')
                count = conn.execute(count_query).scalar()
                empty_tables[table] = count == 0
            else:
                empty_tables[table] = None
    
    return [table for table, is_empty in empty_tables.items() if is_empty]

# Devuelve el directorio más reciente
def list_files_in_most_recent_date(directory):
    date_dirs = [d for d in directory.iterdir() if d.is_dir()]
    most_recent_dir = max(date_dirs, key=lambda d: datetime.strptime(d.name, "%d%m%Y"))
    files = [f for f in most_recent_dir.iterdir() if f.is_file()]
    return most_recent_dir.name, files

def incremental_data(ruta_directorio, fichero_mas_reciente, prefix):
    recent_dir = ruta_directorio / fichero_mas_reciente
    excel_files = [f for f in recent_dir.iterdir() if f.is_file() and f.name.startswith(prefix) and (f.name.endswith('.xls') or f.name.endswith('.xlsx'))]
    
    if not excel_files:
        return pd.DataFrame()
    
    df_list = []
    for file in excel_files:
        df = pd.read_excel(file)
        df_list.append(df)
    
    df_concat = pd.concat(df_list, ignore_index=True)
    
    return df_concat

def are_historical_tables_empty(conn, prefijos_historicos, schema="bronze"):
    empty_tables = {}

    for table_key, table_prefix in prefijos_historicos.items():
        table_name = table_prefix
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

def historical_data(ruta_directorio, prefix):
    excel_files = [f for f in ruta_directorio.iterdir() if f.is_file() and f.name.startswith(prefix) and (f.name.endswith('.xls') or f.name.endswith('.xlsx'))]
    if not excel_files:
        return pd.DataFrame()
    df_list = []
    for file in excel_files:
        df = pd.read_excel(file)
        df_list.append(df)
    
    df_concat = pd.concat(df_list, ignore_index=True)
    
    return df_concat

def delete_old_data(absolute_path):
    try:
        folders = [d for d in os.listdir(absolute_path) if os.path.isdir(os.path.join(absolute_path, d))]
        date_folders = []
        for folder in folders:
            try:
                date = datetime.strptime(folder, "%d%m%Y")
                date_folders.append((folder, date))
            except ValueError:
                continue
        date_folders.sort(key=lambda x: x[1])
        if len(date_folders) > 20:
            while len(date_folders) > 20:
                folder_to_delete, _ = date_folders.pop(0)
                path_to_delete = os.path.join(absolute_path, folder_to_delete)
                shutil.rmtree(path_to_delete)
            return True

        return False

    except Exception:
        return False