DROP TABLE IF EXISTS "Almacenes";
DROP TABLE IF EXISTS "Articulos";
DROP TABLE IF EXISTS "BonosPresencia";
DROP TABLE IF EXISTS "BonosTrabajadas";
DROP TABLE IF EXISTS "Clientes";
DROP TABLE IF EXISTS "Compras";
DROP TABLE IF EXISTS "Empresas";
DROP TABLE IF EXISTS "Invertidas";
DROP TABLE IF EXISTS "Operarios";
DROP TABLE IF EXISTS "Stock";
DROP TABLE IF EXISTS "OrdenesReparacion";
DROP TABLE IF EXISTS "OrdenesVentaMostrador";
DROP TABLE IF EXISTS "OrdenesVentaTaller";
DROP TABLE IF EXISTS "Talleres";
DROP TABLE IF EXISTS "TiposHoras";
DROP TABLE IF EXISTS "TiposOrdenesReparacion";
DROP TABLE IF EXISTS "TiposVentasAlmacen";
DROP TABLE IF EXISTS "Vehiculos";

CREATE TABLE "Almacenes" -- ok data types
(
  "Codigo"    int       NOT NULL,
  "Nombre"    varchar(50)  NOT NULL,
  "Empresa"   int       NOT NULL,
  "FechaCreacion"       TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "Articulos" --ok data types
(
  "Mar"                   int          NOT NULL, -- check
  "Referencia"            varchar(50)  NOT NULL,
  "Articulo"              varchar(50)  NOT NULL,
  "Denominacion"          varchar(50)  NOT NULL,
  "Almacen"               int          NOT NULL,
  "Familia"               varchar(50)  NOT NULL,
  "PVP"                   float        NOT NULL,
  "ClaveDTO"              varchar(50)  ,
  "FechaAlta"             date         ,
  "FechaCreacion"         TIMESTAMP default NOW(),
  "FechaModificacion" 	  TIMESTAMP default NOW()
);

CREATE TABLE "BonosPresencia"  -- okay data types -- okay null values
(
  "Taller"                int       NOT NULL,
  "Fecha"                 date      NOT NULL,
  "Seccion"               varchar(50)  NOT NULL,
  "Operario"              varchar(50)       NOT NULL,
  "NombreOperario"        varchar(250) NOT NULL,
  "EntradaPresencia"      time      ,
  "SalidaPresencia"       time      ,
  "DiferenciaPresencia"   float     ,
  "TipoHora"              varchar(50)  ,
  "FechaCreacion" 		    TIMESTAMP default NOW(),
  "FechaModificacion" 	  TIMESTAMP default NOW()
);

CREATE TABLE "BonosTrabajadas" -- okat data types -- okay null values
(
  "Taller"                int       NOT NULL,
  "Fecha"                 date      NOT NULL,
  "Seccion"               varchar(50)  NOT NULL,
  "Operario"              varchar(50)       NOT NULL,
  "NombreOperario"        varchar(250) NOT NULL,
  "ReferenciaOR"          int       ,
  "TipoOR"                varchar(50)  ,
  "IDV"                   int       ,
  "Matricula"             varchar(50)  ,
  "Entrada"               time      ,
  "Salida"                time      ,
  "DiferenciaTrabajadas"  float     ,
  "FechaCreacion" 		    TIMESTAMP default NOW(),
  "FechaModificacion" 	  TIMESTAMP default NOW()
);

CREATE TABLE "Clientes" -- okay data types
(
  "Codigo"              varchar(50)  NOT NULL,
  "Categoria"           varchar(50)  NOT NULL,
  "Nombre"              varchar(50)  NOT NULL,
  "DNI/CIF"             varchar(50)  ,
  "Direccion"           varchar(250) ,
  "CodigoPostal"        varchar(50)  ,
  "Localidad"           varchar(50)  ,
  "CorreoElectronico"   varchar(100) ,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "Compras" -- okay data types
(
  "Almacen"           int        NOT NULL,
  "Fecha"             date       NOT NULL,
  "ReferenciaCompra"  int        NOT NULL,
  "Cuenta"            varchar(50)   NOT NULL,
  "NombreProveedor"   varchar(250)  NOT NULL,
  "T.com"             varchar(50)   , -- check
  "Albaran"           varchar(50)   ,
  "Articulo"          varchar(50)   NOT NULL,
  "Mar"               varchar(50)   NOT NULL, -- check
  "Articulo1"         varchar(50)   ,
  "Denominacion"      varchar(50)   NOT NULL,
  "Clave"             varchar(50)   ,
  "Familia"           varchar(50)   NOT NULL,
  "Fam.apro"          varchar(50)   , --check
  "F.Market"          varchar(50)   , --check
  "Cantidad"          float      NOT NULL,
  "PrecioCompra"      float      NOT NULL,
  "TotalCompra"       float      NOT NULL,
  "PVP"               float      NOT NULL,
  "FechaCreacion" 		TIMESTAMP default NOW(),
  "FechaModificacion" TIMESTAMP default NOW()
);

CREATE TABLE "Empresas" -- okay data types
(
  "Codigo"              int       NOT NULL,
  "Nombre"              varchar(50)  NOT NULL,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "Invertidas" --okay data types
(
  "Taller"              int       NOT NULL,
  "ReferenciaOR"        int       NOT NULL,
  "FechaApertura"       date      NOT NULL,
  "FechaCierre"         date      NOT NULL,
  "Matricula"           varchar(50)  NOT NULL,
  "CuentaCargo"         varchar(50)  NOT NULL,
  "TipoOR"              varchar(50)  NOT NULL,
  "TipoFactura"         varchar(50)  NOT NULL,
  "Recep"               int       NOT NULL, -- check
  "Operario"            varchar(50)  , -- check
  "TiempoAsignado"      float     NOT NULL,
  "TiempoInvertido"     float     NOT NULL,
  "Bastidor"            varchar(50)  NOT NULL,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "Operarios" --okay data types
(
  "Codigo"              varchar(50)  NOT NULL,
  "Nombre"              varchar(50)  NOT NULL,
  "Seccion"             varchar(50)  NOT NULL,
  "Taller"              int       NOT NULL,
  "Activo"              varchar(50)  NOT NULL,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "Stock" -- ok data types
(
  "Almacen"             int           NOT NULL,
  "Articulo"            varchar(50)      NOT NULL,
  "Mar"                 int           , -- check
  "ReferenciaArticulo"  varchar(50)      NOT NULL,
  "Descripcion"         varchar(250)     NOT NULL,
  "Grupo"               varchar(50)      NOT NULL,
  "Familia"             varchar(50)      NOT NULL,
  "Fam.apro"            varchar(50)      , -- check
  "F.Marketin"          varchar(50)      , -- check
  "ClaveDescuento"      varchar(50)      ,
  "PVP"                 float         NOT NULL,
  "CostoMedio"          float         NOT NULL,
  "Existencia"          float         NOT NULL,
  "ValorStock"          float         NOT NULL,
  "FechaUltimaEntrada"  date          NOT NULL,
  "FechaUltimaSalida"   date          ,
  "Cat"                 varchar(50)      , -- check
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "OrdenesReparacion" -- ok date types
(
  "Taller"                  int       NOT NULL,
  "ReferenciaOR"            int       NOT NULL,
  "IDV"                     int       NOT NULL,
  "Matricula"               varchar(250) NOT NULL,
  "CuentaCargo"             varchar(50)  NOT NULL,
  "NombreCliente"           varchar(250) NOT NULL,
  "DNI/CIF"                 varchar(50)  ,
  "CodigoPostal"            varchar(50)  ,
  "Marca"                   varchar(50)  NOT NULL,
  "TipoOR"                  varchar(50)  NOT NULL,
  "Recep"                   int       NOT NULL, -- check
  "FechaApertura"           date      NOT NULL,
  "HoraCreacion"            time      ,
  "FechaCierre"             date      ,
  "Hora"                    time      ,
  "FechaPrimera"            date      ,
  "FechaUltimo"             date      ,
  "TiempoFacturado"         float     NOT NULL,
  "TiempoInvertido"         float     NOT NULL,
  "DiferenciaTiempo"        float     NOT NULL,
  "Base"                    float     NOT NULL,
  "ManoObra"                float     NOT NULL,
  "ManoObraSub"             float     NOT NULL,
  "Recambio"                float     NOT NULL,
  "CostoManoObra"           float     NOT NULL,
  "CostoSub"                float     NOT NULL,
  "CostoRecambio"           float     NOT NULL,
  "NumeroLocal"             varchar(50)  ,
  "Est"                     varchar(50)  , -- check
  "Serie"                   varchar(50)  ,
  "Bastidor"                varchar(50)  ,
  "CuentaTitular"           varchar(50)  ,
  "FechaCreacion" 		      TIMESTAMP default NOW(),
  "FechaModificacion" 	    TIMESTAMP default NOW()
);

CREATE TABLE "OrdenesVentaMostrador"
(
  "Almacen"                     int       NOT NULL,
  "Referencia"                  int       NOT NULL, -- con esta columna se relaciona con la tabla de ordenes de reparación
  "Serie"                       varchar(50)  NOT NULL,
  "Fecha"                       date      NOT NULL,
  "Cuenta"                      varchar(50)  NOT NULL,
  "NombreCliente"               varchar(150) NOT NULL,
  "DNI/CIF"                     varchar(50)  , -- check 
  "CodigoPostal"                varchar(50)  ,
  "TipoCliente"                 varchar(50)  ,
  "Canal"                       varchar(50)  ,
  "Vendedor"                    varchar(100) , -- check
  "TipoVenta"                   varchar(50)  NOT NULL,
  "Marca"                       varchar(50)  ,
  "Articulo"                    varchar(50)  NOT NULL,
  "Denominacion"                varchar(50)  NOT NULL,
  "Fam.apro"                   varchar(50)  , -- check
  "F.Marketin"                  varchar(50)  , -- check
  "Familia"                     varchar(50)  NOT NULL,
  "Grupo"                       varchar(50)  NOT NULL,
  "Cantidad"                    int       NOT NULL,
  "PVP"                         float     NOT NULL, -- verificar tipo de dato
  "Descuento"                   float     ,
  "Neto"                        float     NOT NULL,
  "Costo"                       float     NOT NULL,
  "PorcentajeBeneficio"         float     NOT NULL,
  "Beneficio"                   float     NOT NULL,
  "FechaCreacion" 		          TIMESTAMP default NOW(),
  "FechaModificacion" 	        TIMESTAMP default NOW()
);

CREATE TABLE "OrdenesVentaTaller" -- ok data types
(
  "Almacen"               int          NOT NULL,
  "ReferenciaVentaTaller" int          NOT NULL,
  "TipoVenta"             varchar(50)  NOT NULL,
  "Recep"                 int          NOT NULL, -- check
  "TipoCliente"           int          ,
  "Cuenta"                varchar(50)  ,
  "NombreCliente"         varchar(50)  ,
  "DNI/CIF"               varchar(50)  ,
  "CodigoPostal"          varchar(50)  ,
  "FechaSalida"           date      ,
  "FechaCierre"           date      ,
  "Articulo"              varchar(250) ,
  "Denominacion"          varchar(50)  ,
  "Familia"               varchar(50)  ,
  "Fam.a"                 varchar(50)  , -- check
  "F.Marketin"            varchar(50)  , -- check
  "Grupo"                 varchar(50)  ,
  "ClaveDescuento"        varchar(50)  ,
  "Cantidad"              float     NOT NULL,
  "PVP"                   float     NOT NULL,
  "Descuento"             float     ,
  "Neto"                  float     NOT NULL,
  "Costo"                 float     NOT NULL,
  "Beneficio"             float     NOT NULL,
  "FechaCreacion" 		    TIMESTAMP default NOW(),
  "FechaModificacion" 	  TIMESTAMP default NOW()
);

CREATE TABLE "Talleres"  -- ok data types
(
  "Codigo"              int       NOT NULL,
  "Nombre"              varchar(50)  NOT NULL,
  "Empresa"             int       NOT NULL,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "TiposHoras" -- ok data types
(
  "Codigo"              varchar(50)  NOT NULL,
  "Descripcion"         varchar(50)  NOT NULL,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "TiposOrdenesReparacion" -- no hay el df
(
  "Codigo"              varchar(50)  NOT NULL,
  "Descripcion"         varchar(50)  NOT NULL,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "TiposVentasAlmacen"  --ok data types
(
  "Codigo"              varchar(50)  NOT NULL,
  "Descripcion"         varchar(50)  NOT NULL,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "Vehiculos"  --ok data types
(
  "IDV"                   int          NOT NULL,
  "Matricula"             varchar(750)  ,
  "Bastidor"              varchar(750)  NOT NULL,
  "Mar"                   varchar(750)  NOT NULL, -- check
  "Modelo"                varchar(750)  ,
  "CuentaTitular"         varchar(750)  NOT NULL,
  "CuentaCliente"         varchar(750)  NOT NULL,
  "CuentaConductor"       varchar(750)  ,
  "FechaMatriculacion"    date          ,
  "Kilometros"            bigint        ,
  "FechaUltimaVisita"     date          ,
  "Familia"               varchar(750)  ,
  "CodigoModelo"          varchar(750)  , 
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);
