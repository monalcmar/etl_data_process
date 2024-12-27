# Diccionario para Almacenes
almacenes_info = {
    'Codigo': {'data_type': int, 'nullable': False},
    'Nombre': {'data_type': str, 'nullable': False},
    'Empresa': {'data_type': int, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para Articulos
articulos_info = {
    'Mar': {'data_type': int, 'nullable': False},
    'Referencia': {'data_type': str, 'nullable': False},
    'Articulo': {'data_type': str, 'nullable': False},
    'Denominacion': {'data_type': str, 'nullable': False},
    'Almacen': {'data_type': int, 'nullable': False},
    'Familia': {'data_type': str, 'nullable': False},
    'PVP': {'data_type': float, 'nullable': False},
    'ClaveDTO': {'data_type': str, 'nullable': True},
    'FechaAlta': {'data_type': 'datetime64[ns]', 'nullable': True}
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para BonosPresencia
bonos_presencia_info = {
    'Taller': {'data_type': int, 'nullable': False},
    'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
    'Seccion': {'data_type': str, 'nullable': False},
    'Operario': {'data_type': int, 'nullable': False},
    'NombreOperario': {'data_type': str, 'nullable': False},
    'EntradaPresencia': {'data_type': 'timedelta64[ns]', 'nullable': True},
    'SalidaPresencia': {'data_type': 'timedelta64[ns]', 'nullable': True},
    'DiferenciaPresencia': {'data_type': float, 'nullable': True},
    'TipoHora': {'data_type': str, 'nullable': True},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para BonosTrabajadas
bonos_trabajadas_info = {
    'Taller': {'data_type': int, 'nullable': False},
    'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
    'Seccion': {'data_type': str, 'nullable': False},
    'Operario': {'data_type': int, 'nullable': False},
    'NombreOperario': {'data_type': str, 'nullable': False},
    'ReferenciaOR': {'data_type': int, 'nullable': True},
    'TipoOR': {'data_type': str, 'nullable': True},
    'IDV': {'data_type': int, 'nullable': True},
    'Matricula': {'data_type': str, 'nullable': True},
    'Entrada': {'data_type': 'timedelta64[ns]', 'nullable': True},
    'Salida': {'data_type': 'timedelta64[ns]', 'nullable': True},
    'DiferenciaTrabajadas': {'data_type': float, 'nullable': True},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para Clientes
clientes_info = {
    'Codigo': {'data_type': str, 'nullable': False},
    'Categoria': {'data_type': str, 'nullable': False},
    'Nombre': {'data_type': str, 'nullable': False},
    'DNI/CIF': {'data_type': str, 'nullable': True},
    'Direccion': {'data_type': str, 'nullable': True},
    'CodigoPostal': {'data_type': str, 'nullable': True},
    'Localidad': {'data_type': str, 'nullable': True},
    'CorreoElectronico': {'data_type': str, 'nullable': True},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para Compras
compras_info = {
    'Almacen': {'data_type': int, 'nullable': False},
    'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
    'ReferenciaCompra': {'data_type': int, 'nullable': False},
    'Cuenta': {'data_type': str, 'nullable': False},
    'NombreProveedor': {'data_type': str, 'nullable': False},
    'T.com': {'data_type': str, 'nullable': True},
    'Albaran': {'data_type': str, 'nullable': True},
    'Articulo': {'data_type': str, 'nullable': False},
    'Mar': {'data_type': str, 'nullable': False},
    'Articulo1': {'data_type': str, 'nullable': True},
    'Denominacion': {'data_type': str, 'nullable': False},
    'Clave': {'data_type': str, 'nullable': True},
    'Familia': {'data_type': str, 'nullable': False},
    'Fam.apro': {'data_type': str, 'nullable': True},
    'F.Market': {'data_type': str, 'nullable': True},
    'Cantidad': {'data_type': float, 'nullable': False},
    'PrecioCompra': {'data_type': float, 'nullable': False},
    'TotalCompra': {'data_type': float, 'nullable': False},
    'PVP': {'data_type': float, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para Empresas
empresas_info = {
    'Codigo': {'data_type': int, 'nullable': False},
    'Nombre': {'data_type': str, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para Invertidas
invertidas_info = {
    "Taller": {"data_type": int, "nullable": False},
    "ReferenciaOR": {"data_type": int, "nullable": False},
    "FechaApertura": {"data_type": "datetime64[ns]", "nullable": False},
    "FechaCierre": {"data_type": "datetime64[ns]", "nullable": False},
    "Matricula": {"data_type": str, "nullable": False},
    "CuentaCargo": {"data_type": str, "nullable": False},
    "TipoOR": {"data_type": str, "nullable": False},
    "TipoFactura": {"data_type": str, "nullable": False},
    "Recep": {"data_type": int, "nullable": False},  # Asumiendo que 'Recep' es un número entero
    'Operario': {'data_type': str, 'nullable': True},
    "TiempoAsignado": {"data_type": float, "nullable": False},
    "TiempoInvertido": {"data_type": float, "nullable": False},
    "Bastidor": {"data_type": str, "nullable": False},
    # "FechaCreacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"},
    # "FechaModificacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"}
}

# Diccionario para la tabla Operarios
operarios_info = {
    "Codigo": {"data_type": str, "nullable": False},
    "Nombre": {"data_type": str, "nullable": False},
    "Seccion": {"data_type": str, "nullable": False},
    "Taller": {"data_type": int, "nullable": False},
    "Activo": {"data_type": str, "nullable": False},
    # "FechaCreacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"},
    # "FechaModificacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"}
}

# Diccionario para la tabla Stock
stock_info = {
    'Almacen': {'data_type': int, 'nullable': False},
    'Articulo': {'data_type': str, 'nullable': False},
    'Mar': {'data_type': int, 'nullable': True},
    'ReferenciaArticulo': {'data_type': str, 'nullable': False},
    'Descripcion': {'data_type': str, 'nullable': False},
    'Grupo': {'data_type': str, 'nullable': False},
    'Familia': {'data_type': str, 'nullable': False},
    'Fam.apro': {'data_type': str, 'nullable': True},
    'F.Marketin': {'data_type': str, 'nullable': True},
    'ClaveDescuento': {'data_type': str, 'nullable': True},
    'PVP': {'data_type': float, 'nullable': False},
    'CostoMedio': {'data_type': float, 'nullable': False},
    'Existencia': {'data_type': float, 'nullable': False},
    'ValorStock': {'data_type': float, 'nullable': False},
    'FechaUltimaEntrada': {'data_type': 'datetime64[ns]', 'nullable': False},
    'FechaUltimaSalida': {'data_type': 'datetime64[ns]', 'nullable': True},
    'Cat': {'data_type': str, 'nullable': True},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

# Diccionario para la tabla OrdenesReparacion
ordenes_reparacion_info = {
    'Taller': {'data_type': int, 'nullable': False},
    'ReferenciaOR': {'data_type': int, 'nullable': False},
    'IDV': {'data_type': int, 'nullable': False},
    'Matricula': {'data_type': str, 'nullable': False},
    'CuentaCargo': {'data_type': str, 'nullable': False},
    'NombreCliente': {'data_type': str, 'nullable': False},
    'DNI/CIF': {'data_type': str, 'nullable': True},
    'CodigoPostal': {'data_type': str, 'nullable': True},
    'Marca': {'data_type': str, 'nullable': False},
    'TipoOR': {'data_type': str, 'nullable': False},
    'Recep': {'data_type': int, 'nullable': False},
    'FechaApertura': {'data_type': 'datetime64[ns]', 'nullable': False},
    'HoraCreacion': {'data_type': 'timedelta64[ns]', 'nullable': True},
    'FechaCierre': {'data_type': 'datetime64[ns]', 'nullable': True},
    'Hora': {'data_type': 'timedelta64[ns]', 'nullable': True},
    'FechaPrimera': {'data_type': 'datetime64[ns]', 'nullable': True},
    'FechaUltimo': {'data_type': 'datetime64[ns]', 'nullable': True},
    'TiempoFacturado': {'data_type': float, 'nullable': False},
    'TiempoInvertido': {'data_type': float, 'nullable': False},
    'DiferenciaTiempo': {'data_type': float, 'nullable': False},
    'Base': {'data_type': float, 'nullable': False},
    'ManoObra': {'data_type': float, 'nullable': False},
    'ManoObraSub': {'data_type': float, 'nullable': False},
    'Recambio': {'data_type': float, 'nullable': False},
    'CostoManoObra': {'data_type': float, 'nullable': False},
    'CostoSub': {'data_type': float, 'nullable': False},
    'CostoRecambio': {'data_type': float, 'nullable': False},
    'NumeroLocal': {'data_type': str, 'nullable': True},
    'Est': {'data_type': str, 'nullable': True},
    'Serie': {'data_type': str, 'nullable': True},
    'Bastidor': {'data_type': str, 'nullable': True},
    'CuentaTitular': {'data_type': str, 'nullable': True},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

# Diccionario para la tabla OrdenesVentaMostrador
ordenes_venta_mostrador_info = {
    'Almacen': {'data_type': int, 'nullable': False},
    'Referencia': {'data_type': int, 'nullable': False},
    'Serie': {'data_type': str, 'nullable': False},
    'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
    'Cuenta': {'data_type': str, 'nullable': False},
    'NombreCliente': {'data_type': str, 'nullable': False},
    'DNI/CIF': {'data_type': str, 'nullable': True},
    'CodigoPostal': {'data_type': str, 'nullable': True},
    'TipoCliente': {'data_type': str, 'nullable': True},
    'Canal': {'data_type': str, 'nullable': True},
    'Vendedor': {'data_type': str, 'nullable': True},
    'TipoVenta': {'data_type': str, 'nullable': False},
    'Marca': {'data_type': str, 'nullable': True},
    'Articulo': {'data_type': str, 'nullable': False},
    'Denominacion': {'data_type': str, 'nullable': False},
    'Fam.apro': {'data_type': str, 'nullable': True},
    'F.Marketin': {'data_type': str, 'nullable': True},
    'Familia': {'data_type': str, 'nullable': False},
    'Grupo': {'data_type': str, 'nullable': False},
    'Cantidad': {'data_type': int, 'nullable': False},
    'PVP': {'data_type': float, 'nullable': False},
    'Descuento': {'data_type': float, 'nullable': True},
    'Neto': {'data_type': float, 'nullable': False},
    'Costo': {'data_type': float, 'nullable': False},
    'PorcentajeBeneficio': {'data_type': float, 'nullable': False},
    'Beneficio': {'data_type': float, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

# Diccionario para OrdenesVentaTaller
ordenes_venta_taller_info = {
    'Almacen': {'data_type': int, 'nullable': False},
    'ReferenciaVentaTaller': {'data_type': int, 'nullable': False},
    'TipoVenta': {'data_type': str, 'nullable': False},
    'Recep': {'data_type': int, 'nullable': False},
    'TipoCliente': {'data_type': int, 'nullable': True},
    'Cuenta': {'data_type': str, 'nullable': True},
    'NombreCliente': {'data_type': str, 'nullable': True},
    'DNI/CIF': {'data_type': str, 'nullable': True},
    'CodigoPostal': {'data_type': str, 'nullable': True},
    'FechaSalida': {'data_type': 'datetime64[ns]', 'nullable': True},
    'FechaCierre': {'data_type': 'datetime64[ns]', 'nullable': True},
    'Articulo': {'data_type': str, 'nullable': True},
    'Denominacion': {'data_type': str, 'nullable': True},
    'Familia': {'data_type': str, 'nullable': True},
    'Fam.a': {'data_type': str, 'nullable': True},
    'F.Marketin': {'data_type': str, 'nullable': True},
    'Grupo': {'data_type': str, 'nullable': True},
    'ClaveDescuento': {'data_type': str, 'nullable': True},
    'Cantidad': {'data_type': float, 'nullable': False},
    'PVP': {'data_type': float, 'nullable': False},
    'Descuento': {'data_type': float, 'nullable': True},
    'Neto': {'data_type': float, 'nullable': False},
    'Costo': {'data_type': float, 'nullable': False},
    'Beneficio': {'data_type': float, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
}

# Diccionario para la tabla Talleres
talleres_info = {
    'Codigo': {'data_type': int, 'nullable': False},
    'Nombre': {'data_type': str, 'nullable': False},
    'Empresa': {'data_type': int, 'nullable': False},
#     'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
#     'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

# Diccionario para la tabla TiposHoras
tipos_horas_info = {
    'Codigo': {'data_type': str, 'nullable': False},
    'Descripcion': {'data_type': str, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

# Diccionario para la tabla TiposOrdenesReparacion
tipos_ordenes_reparacion_info = {
    'Codigo': {'data_type': str, 'nullable': False},
    'Descripcion': {'data_type': str, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

# Diccionario para la tabla TiposVentasAlmacen
tipos_ventas_almacen_info = {
    'Codigo': {'data_type': str, 'nullable': False},
    'Descripcion': {'data_type': str, 'nullable': False},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

# Diccionario para la tabla Vehiculos
vehiculos_info = {
    'IDV': {'data_type': int, 'nullable': False},
    'Matricula': {'data_type': str, 'nullable': True},
    'Bastidor': {'data_type': str, 'nullable': False},
    'Mar': {'data_type': str, 'nullable': False},
    'Modelo': {'data_type': int, 'nullable': True},
    'CuentaTitular': {'data_type': str, 'nullable': False},
    'CuentaCliente': {'data_type': str, 'nullable': False},
    'CuentaConductor': {'data_type': str, 'nullable': True},
    'FechaMatriculacion': {'data_type': 'date', 'nullable': True},
    'Kilometros': {'data_type': int, 'nullable': False},
    'FechaUltimaVisita': {'data_type': 'date', 'nullable': True},
    'Familia': {'data_type': int, 'nullable': True},
    'CodigoModelo': {'data_type': str, 'nullable': True},
    # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
    # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
}

silver_properties = {
    'Almacenes': {
        'Codigo': {'data_type': int, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        'Empresa': {'data_type': int, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'Articulos': {
        'Mar': {'data_type': int, 'nullable': False},
        'Referencia': {'data_type': str, 'nullable': False},
        'Articulo': {'data_type': str, 'nullable': False},
        'Denominacion': {'data_type': str, 'nullable': False},
        'Almacen': {'data_type': int, 'nullable': False},
        'Familia': {'data_type': str, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        'ClaveDTO': {'data_type': str, 'nullable': True},
        'FechaAlta': {'data_type': 'datetime64[ns]', 'nullable': True}
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'Clientes': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Categoria': {'data_type': str, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        'DNI/CIF': {'data_type': str, 'nullable': True},
        'Direccion': {'data_type': str, 'nullable': True},
        'CodigoPostal': {'data_type': str, 'nullable': True},
        'Localidad': {'data_type': str, 'nullable': True},
        'CorreoElectronico': {'data_type': str, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'Empresas': {
        'Codigo': {'data_type': int, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'Operarios': {
        "Codigo": {"data_type": str, "nullable": False},
        "Nombre": {"data_type": str, "nullable": False},
        "Seccion": {"data_type": str, "nullable": False},
        "Taller": {"data_type": int, "nullable": False},
        "Activo": {"data_type": str, "nullable": False},
        # "FechaCreacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"},
        # "FechaModificacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"}
    },
    'Talleres': {
        'Codigo': {'data_type': int, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        'Empresa': {'data_type': int, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'TiposHoras': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Descripcion': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'TiposOrdenesReparacion': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Descripcion': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'TiposVentasAlmacen': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Descripcion': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'Vehiculos': {
        'IDV': {'data_type': int, 'nullable': False},
        'Matricula': {'data_type': str, 'nullable': True},
        'Bastidor': {'data_type': str, 'nullable': False},
        'Mar': {'data_type': str, 'nullable': False},
        'Modelo': {'data_type': int, 'nullable': True},
        'CuentaTitular': {'data_type': str, 'nullable': False},
        'CuentaCliente': {'data_type': str, 'nullable': False},
        'CuentaConductor': {'data_type': str, 'nullable': True},
        'FechaMatriculacion': {'data_type': 'date', 'nullable': True},
        'Kilometros': {'data_type': int, 'nullable': False},
        'FechaUltimaVisita': {'data_type': 'date', 'nullable': True},
        'Familia': {'data_type': int, 'nullable': True},
        'CodigoModelo': {'data_type': str, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'BonosPresencia': {
        'Taller': {'data_type': int, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        'Seccion': {'data_type': str, 'nullable': False},
        'Operario': {'data_type': str, 'nullable': False},
        'NombreOperario': {'data_type': str, 'nullable': False},
        'EntradaPresencia': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'SalidaPresencia': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'DiferenciaPresencia': {'data_type': float, 'nullable': True},
        'TipoHora': {'data_type': str, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'BonosTrabajadas': {
        'Taller': {'data_type': int, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        'Seccion': {'data_type': str, 'nullable': False},
        'Operario': {'data_type': str, 'nullable': False},
        'NombreOperario': {'data_type': str, 'nullable': False},
        'ReferenciaOR': {'data_type': int, 'nullable': True},
        'TipoOR': {'data_type': str, 'nullable': True},
        'IDV': {'data_type': int, 'nullable': True},
        'Matricula': {'data_type': str, 'nullable': True},
        'Entrada': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'Salida': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'DiferenciaTrabajadas': {'data_type': float, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'Compras': {
        'Almacen': {'data_type': int, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        'ReferenciaCompra': {'data_type': int, 'nullable': False},
        'Cuenta': {'data_type': str, 'nullable': False},
        'NombreProveedor': {'data_type': str, 'nullable': False},
        'T.com': {'data_type': str, 'nullable': True},
        'Albaran': {'data_type': str, 'nullable': True},
        'Articulo': {'data_type': str, 'nullable': False},
        'Mar': {'data_type': str, 'nullable': False},
        'Articulo1': {'data_type': str, 'nullable': True},
        'Denominacion': {'data_type': str, 'nullable': False},
        'Clave': {'data_type': str, 'nullable': True},
        'Familia': {'data_type': str, 'nullable': False},
        'Fam.apro': {'data_type': str, 'nullable': True},
        'F.Market': {'data_type': str, 'nullable': True},
        'Cantidad': {'data_type': float, 'nullable': False},
        'PrecioCompra': {'data_type': float, 'nullable': False},
        'TotalCompra': {'data_type': float, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'Invertidas': {
        "Taller": {"data_type": int, "nullable": False},
        "ReferenciaOR": {"data_type": int, "nullable": False},
        "FechaApertura": {"data_type": "datetime64[ns]", "nullable": False},
        "FechaCierre": {"data_type": "datetime64[ns]", "nullable": False},
        "Matricula": {"data_type": str, "nullable": False},
        "CuentaCargo": {"data_type": str, "nullable": False},
        "TipoOR": {"data_type": str, "nullable": False},
        "TipoFactura": {"data_type": str, "nullable": False},
        "Recep": {"data_type": int, "nullable": False},  # Asumiendo que 'Recep' es un número entero
        'Operario': {'data_type': str, 'nullable': True},
        "TiempoAsignado": {"data_type": float, "nullable": False},
        "TiempoInvertido": {"data_type": float, "nullable": False},
        "Bastidor": {"data_type": str, "nullable": False},
        # "FechaCreacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"},
        # "FechaModificacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"}
    },
    'Stock': {
        'Almacen': {'data_type': int, 'nullable': False},
        'Articulo': {'data_type': str, 'nullable': False},
        'Mar': {'data_type': int, 'nullable': True},
        'ReferenciaArticulo': {'data_type': str, 'nullable': False},
        'Descripcion': {'data_type': str, 'nullable': False},
        'Grupo': {'data_type': str, 'nullable': False},
        'Familia': {'data_type': str, 'nullable': False},
        'Fam.apro': {'data_type': str, 'nullable': True},
        'F.Marketin': {'data_type': str, 'nullable': True},
        'ClaveDescuento': {'data_type': str, 'nullable': True},
        'PVP': {'data_type': float, 'nullable': False},
        'CostoMedio': {'data_type': float, 'nullable': False},
        'Existencia': {'data_type': float, 'nullable': False},
        'ValorStock': {'data_type': float, 'nullable': False},
        'FechaUltimaEntrada': {'data_type': 'datetime64[ns]', 'nullable': False},
        'FechaUltimaSalida': {'data_type': 'datetime64[ns]', 'nullable': True},
        'Cat': {'data_type': str, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'OrdenesReparacion': {
        'Taller': {'data_type': int, 'nullable': False},
        'ReferenciaOR': {'data_type': int, 'nullable': False},
        'IDV': {'data_type': int, 'nullable': False},
        'Matricula': {'data_type': str, 'nullable': False},
        'CuentaCargo': {'data_type': str, 'nullable': False},
        'NombreCliente': {'data_type': str, 'nullable': False},
        'DNI/CIF': {'data_type': str, 'nullable': True},
        'CodigoPostal': {'data_type': str, 'nullable': True},
        'Marca': {'data_type': str, 'nullable': False},
        'TipoOR': {'data_type': str, 'nullable': False},
        'Recep': {'data_type': int, 'nullable': False},
        'FechaApertura': {'data_type': 'datetime64[ns]', 'nullable': False},
        'HoraCreacion': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'FechaCierre': {'data_type': 'datetime64[ns]', 'nullable': True},
        'Hora': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'FechaPrimera': {'data_type': 'datetime64[ns]', 'nullable': True},
        'FechaUltimo': {'data_type': 'datetime64[ns]', 'nullable': True},
        'TiempoFacturado': {'data_type': float, 'nullable': False},
        'TiempoInvertido': {'data_type': float, 'nullable': False},
        'DiferenciaTiempo': {'data_type': float, 'nullable': False},
        'Base': {'data_type': float, 'nullable': False},
        'ManoObra': {'data_type': float, 'nullable': False},
        'ManoObraSub': {'data_type': float, 'nullable': False},
        'Recambio': {'data_type': float, 'nullable': False},
        'CostoManoObra': {'data_type': float, 'nullable': False},
        'CostoSub': {'data_type': float, 'nullable': False},
        'CostoRecambio': {'data_type': float, 'nullable': False},
        'NumeroLocal': {'data_type': str, 'nullable': True},
        'Est': {'data_type': str, 'nullable': True},
        'Serie': {'data_type': str, 'nullable': True},
        'Bastidor': {'data_type': str, 'nullable': True},
        'CuentaTitular': {'data_type': str, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'OrdenesVentaMostrador': {
        'Almacen': {'data_type': int, 'nullable': False},
        'Referencia': {'data_type': int, 'nullable': False},
        'Serie': {'data_type': str, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        'Cuenta': {'data_type': str, 'nullable': False},
        'NombreCliente': {'data_type': str, 'nullable': False},
        'DNI/CIF': {'data_type': str, 'nullable': True},
        'CodigoPostal': {'data_type': str, 'nullable': True},
        'TipoCliente': {'data_type': str, 'nullable': True},
        'Canal': {'data_type': str, 'nullable': True},
        'Vendedor': {'data_type': str, 'nullable': True},
        'TipoVenta': {'data_type': str, 'nullable': False},
        'Marca': {'data_type': str, 'nullable': True},
        'Articulo': {'data_type': str, 'nullable': False},
        'Denominacion': {'data_type': str, 'nullable': False},
        'Fam.apro': {'data_type': str, 'nullable': True},
        'F.Marketin': {'data_type': str, 'nullable': True},
        'Familia': {'data_type': str, 'nullable': False},
        'Grupo': {'data_type': str, 'nullable': False},
        'Cantidad': {'data_type': int, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        'Descuento': {'data_type': float, 'nullable': True},
        'Neto': {'data_type': float, 'nullable': False},
        'Costo': {'data_type': float, 'nullable': False},
        'PorcentajeBeneficio': {'data_type': float, 'nullable': False},
        'Beneficio': {'data_type': float, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'OrdenesVentaTaller': {
        'Almacen': {'data_type': int, 'nullable': False},
        'ReferenciaVentaTaller': {'data_type': int, 'nullable': False},
        'TipoVenta': {'data_type': str, 'nullable': False},
        'Recep': {'data_type': int, 'nullable': False},
        'TipoCliente': {'data_type': int, 'nullable': True},
        'Cuenta': {'data_type': str, 'nullable': True},
        'NombreCliente': {'data_type': str, 'nullable': True},
        'DNI/CIF': {'data_type': str, 'nullable': True},
        'CodigoPostal': {'data_type': str, 'nullable': True},
        'FechaSalida': {'data_type': 'datetime64[ns]', 'nullable': True},
        'FechaCierre': {'data_type': 'datetime64[ns]', 'nullable': True},
        'Articulo': {'data_type': str, 'nullable': True},
        'Denominacion': {'data_type': str, 'nullable': True},
        'Familia': {'data_type': str, 'nullable': True},
        'Fam.a': {'data_type': str, 'nullable': True},
        'F.Marketin': {'data_type': str, 'nullable': True},
        'Grupo': {'data_type': str, 'nullable': True},
        'ClaveDescuento': {'data_type': str, 'nullable': True},
        'Cantidad': {'data_type': float, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        'Descuento': {'data_type': float, 'nullable': True},
        'Neto': {'data_type': float, 'nullable': False},
        'Costo': {'data_type': float, 'nullable': False},
        'Beneficio': {'data_type': float, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    }
}

gold_properties = {
    'Almacenes': {
        'Codigo': {'data_type': int, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        'FkEmpresa': {'data_type': int, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Articulos': {
        'Mar': {'data_type': int, 'nullable': False},
        'Referencia': {'data_type': str, 'nullable': False},
        'Articulo': {'data_type': str, 'nullable': False},
        'Denominacion': {'data_type': str, 'nullable': False},
        'FkAlmacen': {'data_type': int, 'nullable': True},
        'Familia': {'data_type': str, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        'ClaveDTO': {'data_type': str, 'nullable': True},
        'FechaAlta': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Clientes': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Categoria': {'data_type': str, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        'DNI/CIF': {'data_type': str, 'nullable': True},
        'Direccion': {'data_type': str, 'nullable': True},
        'CodigoPostal': {'data_type': str, 'nullable': True},
        'Localidad': {'data_type': str, 'nullable': True},
        'CorreoElectronico': {'data_type': str, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Empresas': {
        'Codigo': {'data_type': int, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True}
    },
    'Vehiculos': {
        'IDV': {'data_type': int, 'nullable': False},
        'Matricula': {'data_type': str, 'nullable': True},
        'Bastidor': {'data_type': str, 'nullable': False},
        'Mar': {'data_type': str, 'nullable': False},
        'Modelo': {'data_type': int, 'nullable': True},
        'FkCuentaTitular': {'data_type': int, 'nullable': False},
        'FkCuentaCliente': {'data_type': int, 'nullable': False},
        'FkCuentaConductor': {'data_type': int, 'nullable': True},
        'FechaMatriculacion': {'data_type': 'date', 'nullable': True},
        'Kilometros': {'data_type': int, 'nullable': False},
        'FechaUltimaVisita': {'data_type': 'datetime64[ns]', 'nullable': True},
        'Familia': {'data_type': int, 'nullable': True},
        'CodigoModelo': {'data_type': str, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Operarios': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        'Seccion': {'data_type': str, 'nullable': False},
        'FkTaller': {'data_type': int, 'nullable': False},
        'Activo': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Talleres': {
        'Codigo': {'data_type': int, 'nullable': False},
        'Nombre': {'data_type': str, 'nullable': False},
        'FkEmpresa': {'data_type': int, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'BonosPresencia': {
        'FkTaller': {'data_type': int, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        # 'Seccion': {'data_type': str, 'nullable': False},
        'FkOperario': {'data_type': int, 'nullable': False},
        # 'NombreOperario': {'data_type': str, 'nullable': False},
        'EntradaPresencia': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'SalidaPresencia': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'DiferenciaPresencia': {'data_type': float, 'nullable': True},
        'FkTipoHoras': {'data_type': int, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'BonosTrabajadas': {
        # 'FkTaller': {'data_type': int, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        # 'Seccion': {'data_type': str, 'nullable': False},
        'FkOperario': {'data_type': int, 'nullable': False},
        # 'NombreOperario': {'data_type': str, 'nullable': False},
        'FkOrdenReparacion': {'data_type': int, 'nullable': False},
        # 'TipoOR': {'data_type': str, 'nullable': True},
        # 'FkVehiculo': {'data_type': int, 'nullable': True},
        # 'Matricula': {'data_type': str, 'nullable': True},
        'Entrada': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'Salida': {'data_type': 'timedelta64[ns]', 'nullable': True},
        'DiferenciaTrabajadas': {'data_type': float, 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Compras': {
        'FkAlmacen': {'data_type': int, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        'ReferenciaCompra': {'data_type': str, 'nullable': False},
        'FkCuenta': {'data_type': int, 'nullable': False},
        'NombreProveedor': {'data_type': str, 'nullable': False},
        'TipoComprobante': {'data_type': str, 'nullable': True},
        'FkArticulo': {'data_type': int, 'nullable': False},
        'Denominacion': {'data_type': str, 'nullable': False},
        'Cantidad': {'data_type': float, 'nullable': False},
        'PrecioCompra': {'data_type': float, 'nullable': False},
        'TotalCompra': {'data_type': float, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Invertidas': {
        # "Taller": {"data_type": int, "nullable": False},
        # "ReferenciaOR": {"data_type": int, "nullable": False},
        "FechaApertura": {"data_type": "datetime64[ns]", "nullable": False},
        "FechaCierre": {"data_type": "datetime64[ns]", "nullable": True},
        # "Matricula": {"data_type": str, "nullable": False},
        # "CuentaCargo": {"data_type": str, "nullable": False},
        # "TipoOR": {"data_type": str, "nullable": False},
        "TipoFactura": {"data_type": str, "nullable": False},
        "Recep": {"data_type": str, "nullable": False},  # Asumiendo que 'Recep' es un número entero
        # 'Operario': {'data_type': str, 'nullable': True},
        "TiempoAsignado": {"data_type": float, "nullable": True},
        "TiempoInvertido": {"data_type": float, "nullable": True},
        'FkOperario': {"data_type": int, "nullable": False},
        'FkOrdenReparacion': {"data_type": int, "nullable": False}
        #"Bastidor": {"data_type": str, "nullable": False},
        # "FechaCreacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"},
        # "FechaModificacion": {"data_type": "datetime64[ns]", "nullable": True, "default": "NOW()"}
    },
    'TiposHoras': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Descripcion': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'TiposOrdenesReparacion': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Descripcion': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True, 'default': 'NOW()'}
    },
    'TiposVentasAlmacen': {
        'Codigo': {'data_type': str, 'nullable': False},
        'Descripcion': {'data_type': str, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'OrdenesReparacion': {
        'FkTaller': {'data_type': int, 'nullable': False}, #ok
        'ReferenciaOR': {'data_type': str, 'nullable': False}, #ok
        'FkVehiculo': {'data_type': int, 'nullable': False}, #ok
        'FkCuentaCargo': {'data_type': int, 'nullable': False}, #ok
        'FkCuentaTitular': {'data_type': int, 'nullable': False}, #ok
        'FkTipoOrdenReparacion': {'data_type': int, 'nullable': False}, #ok
        'FechaApertura': {'data_type': 'datetime64[ns]', 'nullable': False}, #ok
        'FechaCierre': {'data_type': 'datetime64[ns]', 'nullable': True}, # ok
        "TiempoFacturado": {'data_type': float, 'nullable': True}, # ok
        "TiempoInvertido": {'data_type': float, 'nullable': True}, # ok
        "Base": {'data_type': float, 'nullable': False}, #ok
        "ManoObra": {'data_type': float, 'nullable': False}, #ok
        "ManoObraSub": {'data_type': float, 'nullable': False}, #ok
        "Recambio": {'data_type': float, 'nullable': False}, #ok
        "CostoManoObra": {'data_type': float, 'nullable': True}, #ok
        "CostoSub": {'data_type': float, 'nullable': True}, #ok
        "CostoRecambio": {'data_type': float, 'nullable': True}, #ok
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'Stock': {
        'FkAlmacen': {'data_type': int, 'nullable': False},
        'FkArticulo': {'data_type': int, 'nullable': False},
        'Existencia': {'data_type': float, 'nullable': False},
        'CostoMedio': {'data_type': float, 'nullable': False},
        'ValorStock': {'data_type': float, 'nullable': False},
        'FechaUltimaEntrada': {'data_type': 'datetime64[ns]', 'nullable': True},
        'FechaUltimaSalida': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'OrdenesVentaMostrador': {
        'FkAlmacen': {'data_type': int, 'nullable': False},
        'Referencia': {'data_type': str, 'nullable': False},
        'Fecha': {'data_type': 'datetime64[ns]', 'nullable': False},
        'FkCliente': {'data_type': int, 'nullable': False},
        'FkArticulo': {'data_type': int, 'nullable': False},
        'Cantidad': {'data_type': int, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        'Descuento': {'data_type': float, 'nullable': True},
        'Neto': {'data_type': float, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
    'OrdenesVentaTaller': {
        'FkAlmacen': {'data_type': int, 'nullable': False},
        'Referencia': {'data_type': str, 'nullable': False},
        'FkTipoVenta': {'data_type': int, 'nullable': False},
        'FkCliente': {'data_type': int, 'nullable': False},
        'FkArticulo': {'data_type': int, 'nullable': False},
        'Cantidad': {'data_type': int, 'nullable': False},
        'PVP': {'data_type': float, 'nullable': False},
        'Descuento': {'data_type': float, 'nullable': True},
        'Neto': {'data_type': float, 'nullable': False},
        # 'FechaCreacion': {'data_type': 'datetime64[ns]', 'nullable': True},
        # 'FechaModificacion': {'data_type': 'datetime64[ns]', 'nullable': True},
    },
}
