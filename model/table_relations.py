import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.model_info import almacenes_info, articulos_info, bonos_presencia_info
from model.model_info import bonos_trabajadas_info, clientes_info
from model.model_info import compras_info, empresas_info, invertidas_info
from model.model_info import operarios_info, stock_info, ordenes_reparacion_info
from model.model_info import ordenes_venta_mostrador_info, ordenes_venta_taller_info
from model.model_info import talleres_info, tipos_horas_info, tipos_ordenes_reparacion_info
from model.model_info import tipos_ventas_almacen_info, vehiculos_info

column_mappings = {
    # Master
    'U6321303_Almacenes': almacenes_info,
    'U6301303_Articulos': articulos_info,
    'U6301303_Clientes': clientes_info,
    'U6311303_Empresas': empresas_info,
    'U6331303_Operarios': operarios_info,
    'U6311303_Talleres': talleres_info,
    'ULSTTHPT_TiposHoras': tipos_horas_info,
    'ULSTTVPT_TiposVentas': tipos_ventas_almacen_info,
    'U6341303_Vehiculos': vehiculos_info,

    # Fact Tables
    'U551_Presencia': bonos_presencia_info,
    'U532_Trabajadas': bonos_trabajadas_info,
    'U553_Compras': compras_info,
    'U555_Invertidas': invertidas_info,
    'U552_Stock': stock_info,
    'U533_OrdenesReparacion': ordenes_reparacion_info,
    'U554_VentasMostrador': ordenes_venta_mostrador_info,
    'U560_VentasTaller': ordenes_venta_taller_info
}


related_orig_bron = {
    'master_table':[
        {
            'df_orig': 'df_almacenes', 
            'tbl_bron': 'U6321303_Almacenes',
            'key_columns': ['Codi'],
            'date_column': None},
        {
            'df_orig': 'df_cliente',
            'tbl_bron': 'U6301303_Clientes',
            'key_columns': ['Codigo cuenta'],
            'date_column': None},
        {
            'df_orig': 'df_empresas',
            'tbl_bron': 'U6311303_Empresas',
            'key_columns': ['Codig'],
            'date_column': None},
        {
            'df_orig': 'df_operarios',
            'tbl_bron': 'U6331303_Operarios',
            'key_columns': ['Codigo'],
            'date_column': None},
        {
            'df_orig': 'df_talleres',
            'tbl_bron': 'U6311303_Talleres',
            'key_columns': ['Codig'],
            'date_column': None},
        {
            'df_orig': 'df_tipos_horas',
            'tbl_bron': 'ULSTTHPT_TiposHoras',
            'key_columns': ['Codigo'],
            'date_column': None},
        {
            'df_orig': 'df_tipos_ordenes',
            'tbl_bron': 'UU2_TiposOrdenes',
            'key_columns': ['Codigo'],
            'date_column': None},
        {
            'df_orig': 'df_tipos_venta',
            'tbl_bron': 'ULSTTVPT_TiposVentas',
            'key_columns': ['Codigo'],
            'date_column': None},
        {
            'df_orig': 'df_vehiculos',
            'tbl_bron': 'U6341303_Vehiculos',
            'key_columns': ['Bastidor'],
            'date_column': None}
        ],
    'master_table_mult':[
        {
            'df_orig': 'df_articulos',
            'tbl_bron': 'U6301303_Articulos',
            'key_columns': ['Ref.articulo', 'Articulo', 'Alma'],
            'date_column': None},
    ],
    'fact_table': [
        {
            'df_orig': 'df_taller_orden_rep',
            'tbl_bron': 'U533_OrdenesReparacion', 
            'key_columns': ['REF.OR'],
            'date_column': 'Fec.apertu'},
        {
            'df_orig': 'df_mostrador',
            'tbl_bron': 'U554_VentasMostrador', 
            'key_columns': ['Refer.'],
            'date_column': 'Fecha'},
        {
            'df_orig': 'df_taller_orden_venta',
            'tbl_bron': 'U560_VentasTaller', 
            'key_columns': ['Refer.'],
            'date_column': 'Fec.sali'}
    ],
    'fact_table_mult': [
        {
            'df_orig': 'df_bono_pres',
            'tbl_bron': 'U551_Presencia', 
            'key_columns': ['Operario', 'ENTRADA PRES'],
            'date_column': 'Fecha'},
        {
            'df_orig': 'df_bonos_trab',
            'tbl_bron': 'U532_Trabajadas', 
            'key_columns': ['Operario', 'Entra'],
            'date_column': 'Fecha'},
        {
            'df_orig': 'df_compras',
            'tbl_bron': 'U553_Compras', 
            'key_columns': ['Referenci', 'Artículo'],
            'date_column': 'Fecha'},
        {
            'df_orig': 'df_invertidas',
            'tbl_bron': 'U555_Invertidas', 
            'key_columns': ['REF.OR', 'Operario'],
            'date_column': 'Fec.apertu'},
        {
            'df_orig': 'df_stock',
            'tbl_bron': 'U552_Stock', 
            'key_columns': ['Alma', 'Ref.articulo'],
            'date_column': 'F.ul.ent'}        
    ]
}



related_bron_silv = {
    'master_table':[
        {'tbl_bron': 'U6321303_Almacenes', 
         'tbl_silv': 'Almacenes', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'U6301303_Clientes', 
         'tbl_silv': 'Clientes', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'U6311303_Empresas', 
         'tbl_silv': 'Empresas', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'U6331303_Operarios', 
         'tbl_silv': 'Operarios', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'U6311303_Talleres', 
         'tbl_silv': 'Talleres', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'ULSTTHPT_TiposHoras', 
         'tbl_silv': 'TiposHoras', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'UU2_TiposOrdenes', 
         'tbl_silv': 'TiposOrdenesReparacion', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'ULSTTVPT_TiposVentas', 
         'tbl_silv': 'TiposVentasAlmacen', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_bron': 'U6341303_Vehiculos', 
         'tbl_silv': 'Vehiculos', 
         'key_columns': ['Bastidor'],
         'date_column': None}
        ],
    'master_table_mult':[
        {'tbl_bron': 'U6301303_Articulos', 
         'tbl_silv': 'Articulos', 
         'key_columns': ['Referencia', 'Articulo', 'Almacen'],
         'date_column': None},
    ],
    'fact_table': [
        {'tbl_bron': 'U533_OrdenesReparacion', 
         'tbl_silv': 'OrdenesReparacion', 
         'key_columns': ['ReferenciaOR'],
         'date_column': 'FechaApertura'},
        {'tbl_bron': 'U554_VentasMostrador', 
         'tbl_silv': 'OrdenesVentaMostrador', 
         'key_columns': ['Referencia'],
         'date_column': 'Fecha'},
        {'tbl_bron': 'U560_VentasTaller', 
         'tbl_silv': 'OrdenesVentaTaller', 
         'key_columns': ['ReferenciaVentaTaller'],
         'date_column': 'FechaSalida'}
    ],
    'fact_table_mult': [
        {'tbl_bron': 'U551_Presencia', 
         'tbl_silv': 'BonosPresencia', 
         'key_columns': ['Operario', 'EntradaPresencia'],
         'date_column': 'Fecha'},
        {'tbl_bron': 'U532_Trabajadas', 
         'tbl_silv': 'BonosTrabajadas', 
         'key_columns': ['Operario', 'Entrada'],
         'date_column': 'Fecha'},
        {'tbl_bron': 'U553_Compras', 
         'tbl_silv': 'Compras', 
         'key_columns': ['ReferenciaCompra', 'Articulo'],
         'date_column': 'Fecha'},
        {'tbl_bron': 'U555_Invertidas', 
         'tbl_silv': 'Invertidas', 
         'key_columns': ['ReferenciaOR', 'Operario'],
         'date_column': 'FechaApertura'},
        {'tbl_bron': 'U552_Stock', 
         'tbl_silv': 'Stock', 
         'key_columns': ['Almacen', 'ReferenciaArticulo'],
         'date_column': 'FechaUltimaEntrada'}        
    ]
}

related_silv_gold = {
    'master_table':[
        {'tbl_silv': 'Almacenes', 
         'tbl_gold': 'Almacenes', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_silv': 'Clientes', 
         'tbl_gold': 'Clientes', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_silv': 'Empresas', 
         'tbl_gold': 'Empresas', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_silv': 'Operarios', 
         'tbl_gold': 'Operarios', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_silv': 'Talleres', 
         'tbl_gold': 'Talleres', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_silv': 'TiposHoras', 
         'tbl_gold': 'TiposHoras', 
         'key_columns': ['Codigo'],
         'date_column': None},
         {'tbl_silv': 'TiposVentasAlmacen', 
         'tbl_gold': 'TiposVentasAlmacen', 
         'key_columns': ['Codigo'],
         'date_column': None},
         {'tbl_silv': 'TiposOrdenesReparacion', 
         'tbl_gold': 'TiposOrdenesReparacion', 
         'key_columns': ['Codigo'],
         'date_column': None},
        {'tbl_silv': 'Vehiculos', 
         'tbl_gold': 'Vehiculos', 
         'key_columns': ['Bastidor'],
         'date_column': None}
        ],
    'master_table_mult':[
        {'tbl_silv': 'Articulos', 
         'tbl_gold': 'Articulos', 
         'key_columns': ['Referencia', 'Articulo', 'Almacen'],
         'date_column': None},
    ],
    'fact_table': [
        {'tbl_silv': 'OrdenesReparacion', 
         'tbl_gold': 'OrdenesReparacion', 
         'key_columns': ['ReferenciaOR'],
         'date_column': 'FechaApertura'},
        {'tbl_silv': 'OrdenesVentaMostrador', 
         'tbl_gold': 'OrdenesVentaMostrador', 
         'key_columns': ['Referencia'],
         'date_column': 'Fecha'},
        {'tbl_silv': 'OrdenesVentaTaller', 
         'tbl_gold': 'OrdenesVentaTaller', 
         'key_columns': ['ReferenciaVentaTaller'],
         'date_column': 'FechaSalida'}
    ],
    'fact_table_mult': [
        {'tbl_silv': 'BonosPresencia', 
         'tbl_gold': 'BonosPresencia', 
         'key_columns': ['Operario', 'EntradaPresencia'],
         'date_column': 'Fecha'},
        {'tbl_silv': 'BonosTrabajadas', 
         'tbl_gold': 'BonosTrabajadas', 
         'key_columns': ['Operario', 'Entrada'],
         'date_column': 'Fecha'},
        {'tbl_silv': 'Compras', 
         'tbl_gold': 'Compras', 
         'key_columns': ['ReferenciaCompra', 'Articulo'],
         'date_column': 'Fecha'},
        {'tbl_silv': 'Invertidas', 
         'tbl_gold': 'Invertidas', 
         'key_columns': ['ReferenciaOR', 'Operario'],
         'date_column': 'FechaApertura'},
        {'tbl_silv': 'Stock', 
         'tbl_gold': 'Stock', 
         'key_columns': ['Almacen', 'ReferenciaArticulo'],
         'date_column': 'FechaUltimaEntrada'}        
    ]
}

extract_tbls_bron = {}

related_silv_gold_v2 = {
    'Almacenes':[
        {'tbl_silv': 'Almacenes', 
         'tbl_gold': 'Almacenes',
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'Clientes':[
        {'tbl_silv': 'Clientes', 
         'tbl_gold': 'Clientes', 
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'Empresas':[
        {'tbl_silv': 'Empresas', 
         'tbl_gold': 'Empresas', 
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'Operarios':[
        {'tbl_silv': 'Operarios', 
         'tbl_gold': 'Operarios', 
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'Talleres':[
        {'tbl_silv': 'Talleres', 
         'tbl_gold': 'Talleres', 
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'TiposHoras':[
        {'tbl_silv': 'TiposHoras', 
         'tbl_gold': 'TiposHoras', 
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'TiposVentasAlmacen':[
         {'tbl_silv': 'TiposVentasAlmacen', 
         'tbl_gold': 'TiposVentasAlmacen', 
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'TiposOrdenesReparacion':[
         {'tbl_silv': 'TiposOrdenesReparacion', 
         'tbl_gold': 'TiposOrdenesReparacion', 
         'key_columns': ['Codigo'],
         'date_column': None}
    ],
    'Vehiculos':[
        {'tbl_silv': 'Vehiculos', 
         'tbl_gold': 'Vehiculos', 
         'key_columns': ['Bastidor'],
         'date_column': None}
        ],
    'Articulos':[
        {'tbl_silv': 'Articulos', 
         'tbl_gold': 'Articulos', 
         'key_columns': ['Referencia', 'Articulo', 'FkAlmacen'],
         'date_column': None},
    ],
    'OrdenesReparacion': [
        {'tbl_silv': 'OrdenesReparacion', 
         'tbl_gold': 'OrdenesReparacion', 
         'key_columns': ['ReferenciaOR'],
         'date_column': 'FechaApertura'}
    ],
    'OrdenesVentaMostrador': [
        {'tbl_silv': 'OrdenesVentaMostrador', 
         'tbl_gold': 'OrdenesVentaMostrador', 
         'key_columns': ['Referencia'],
         'date_column': 'Fecha'}
    ],
    'OrdenesVentaTaller': [
        {'tbl_silv': 'OrdenesVentaTaller', 
         'tbl_gold': 'OrdenesVentaTaller', 
         'key_columns': ['ReferenciaVentaTaller'],
         'date_column': 'FechaSalida'}
    ],
    'BonosPresencia': [
        {'tbl_silv': 'BonosPresencia', 
         'tbl_gold': 'BonosPresencia', 
         'key_columns': ['FkOperario', 'EntradaPresencia'],
         'date_column': 'Fecha'}
    ],
    'BonosTrabajadas': [
        {'tbl_silv': 'BonosTrabajadas', 
         'tbl_gold': 'BonosTrabajadas', 
         'key_columns': ['FkOperario', 'Entrada'],
         'date_column': 'Fecha'}
    ],
    'Compras': [
        {'tbl_silv': 'Compras', 
         'tbl_gold': 'Compras', 
         'key_columns': ['ReferenciaCompra', 'Articulo'],
         'date_column': 'Fecha'}
    ],
    'Invertidas': [
        {'tbl_silv': 'Invertidas', 
         'tbl_gold': 'Invertidas', 
         'key_columns': ['FkOrdenReparacion', 'FkOperario'],
         'date_column': 'FechaApertura'}
    ],
    'Stock': [
        {'tbl_silv': 'Stock', 
         'tbl_gold': 'Stock', 
         'key_columns': ['Almacen', 'ReferenciaArticulo'],
         'date_column': 'FechaUltimaEntrada'}
    ]
}