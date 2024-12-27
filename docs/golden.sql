DROP TABLE IF EXISTS "OrdenesVentaTaller";
DROP TABLE IF EXISTS "OrdenesVentaMostrador";
DROP TABLE IF EXISTS "Invertidas";
DROP TABLE IF EXISTS "Compras";
DROP TABLE IF EXISTS "BonosTrabajadas";
DROP TABLE IF EXISTS "OrdenesReparacion";
DROP TABLE IF EXISTS "BonosPresencia";
DROP TABLE IF EXISTS "Stock";
DROP TABLE IF EXISTS "Articulos";
DROP TABLE IF EXISTS "Almacenes";
DROP TABLE IF EXISTS "Operarios";
DROP TABLE IF EXISTS "Talleres";
DROP TABLE IF EXISTS "Vehiculos";
DROP TABLE IF EXISTS "Empresas";

DROP TABLE IF EXISTS "Clientes";
DROP TABLE IF EXISTS "TiposHoras";
DROP TABLE IF EXISTS "TiposVentasAlmacen";
DROP TABLE IF EXISTS "TiposOrdenesReparacion";

CREATE TABLE "Almacenes" (
  "IdAlmacen"           int       NOT NULL,
  "Codigo"              int       NOT NULL,
  "Nombre"              varchar(50)  NOT NULL,
  "FkEmpresa"           int       NOT NULL,
  "FechaCreacion"       TIMESTAMP default NOW(),
  "FechaModificacion"   TIMESTAMP default NOW(),
  PRIMARY KEY ("IdAlmacen")
);

CREATE TABLE "Articulos" (
  "IdArticulo"          int           NOT NULL,
  "Mar"                 int           NOT NULL,
  "Referencia"          varchar(50)   NOT NULL,
  "Articulo"            varchar(50)   NOT NULL,
  "Denominacion"        varchar(50)   NOT NULL,
  "Familia"             varchar(50)   NOT NULL,
  "PVP"                 float         NOT NULL,
  "ClaveDTO"            varchar(50)   ,
  "FechaAlta"           date          ,
  "FkAlmacen"           int           NOT NULL,
  "FechaCreacion"       TIMESTAMP default NOW(),
  "FechaModificacion"   TIMESTAMP default NOW(),
  PRIMARY KEY ("IdArticulo")
);

CREATE TABLE "BonosPresencia" (
  "IdBonoPresencia"      int                 NOT NULL,
  "Fecha"                date                NOT NULL,
  "EntradaPresencia"     time                ,
  "SalidaPresencia"      time,
  "DiferenciaPresencia"  float,
  "FkTipoHoras"          int                 ,
  "FkTaller"             int                 NOT NULL,
  "FkOperario"           int                 NOT NULL,
  "FechaCreacion"        TIMESTAMP default NOW(),
  "FechaModificacion"    TIMESTAMP default NOW(),
  PRIMARY KEY ("IdBonoPresencia")
);

CREATE TABLE "BonosTrabajadas" 
(
  "IdBonoTrabajadas"      int                 NOT NULL,
  "Fecha"                 date                NOT NULL,
  "Entrada"               time                ,
  "Salida"                time                ,
  "DiferenciaTrabajadas"  float               ,
  "FkOperario"            int                 NOT NULL,
  "FkOrdenReparacion"     int                 NOT NULL,
  "FechaCreacion"         TIMESTAMP default NOW(),
  "FechaModificacion"     TIMESTAMP default NOW(),
  PRIMARY KEY ("IdBonoTrabajadas")
);

CREATE TABLE "Clientes" 
(
  "IdCliente"           int       NOT NULL,
  "Codigo"              varchar(50)  NOT NULL,
  "Categoria"           varchar(50)  NOT NULL,
  "Nombre"              varchar(50)  NOT NULL,
  "DNI/CIF"             varchar(50)  ,
  "Direccion"           varchar(250) ,
  "CodigoPostal"        varchar(50)  ,
  "Localidad"           varchar(50)  ,
  "CorreoElectronico"   varchar(100) ,
  "FechaCreacion"       TIMESTAMP default NOW(),
  "FechaModificacion"   TIMESTAMP default NOW(),
  PRIMARY KEY ("IdCliente")
);

CREATE TABLE "Compras" 
(
  "IdCompra"         int       NOT NULL,
  "Fecha"            date      NOT NULL,
  "ReferenciaCompra" varchar(250) NOT NULL,
  -- "NombreProvedor"   varchar(100) NOT NULL, -- Es el nombre de la cuenta
  "T.Com"            float     NOT NULL,
  "Albaran"          varchar(100) NOT NULL,
  "Cantidad"         int       NOT NULL,
  "PrecioCompra"         float     NOT NULL,
  "TotalCompra"      float     NOT NULL,
  -- "PVP"              float     NOT NULL,
  "FkCuenta"         int       NOT NULL,
  "FkAlmacen"        int       NOT NULL,
  -- "FkCliente"        int       NOT NULL,
  "FkArticulo"       int       NOT NULL,
  "FechaCreacion"    TIMESTAMP default NOW(),
  "FechaModificacion" TIMESTAMP default NOW(),
  PRIMARY KEY ("IdCompra")
);

CREATE TABLE "Empresas" 
(
  "IdEmpresa"         int       NOT NULL,
  "Codigo"            int       NOT NULL,
  "Nombre"            varchar(50)  NOT NULL,
  "FechaCreacion"     TIMESTAMP default NOW(),
  "FechaModificacion" TIMESTAMP default NOW(),
  PRIMARY KEY ("IdEmpresa")
);

CREATE TABLE "Invertidas" 
(
  "IdBonoInvertidas"  int      NOT NULL,
  "FechaApertura"     date     NOT NULL,
  "FechaCierre"       date     ,
  "TipoFactura"       varchar(50) NOT NULL,
  "Recep"             varchar(50) NOT NULL,
  "TiempoAsignado"    float    ,
  "TiempoInvertido"   float    ,
  "FkOperario"        int      NOT NULL,
  "FkOrdenReparacion" int      NOT NULL,
  "FechaCreacion"     TIMESTAMP default NOW(),
  "FechaModificacion" TIMESTAMP default NOW(),
  PRIMARY KEY ("IdBonoInvertidas")
);

CREATE TABLE "Operarios" 
(
  "IdOperario"        int       NOT NULL,
  "Codigo"            varchar(50)  NOT NULL,
  "Nombre"            varchar(50)  NOT NULL,
  "Seccion"           varchar(50)  NOT NULL,
  "Activo"            varchar(50)  NOT NULL,
  "FkTaller"          int       NOT NULL,
  "FechaCreacion"     TIMESTAMP default NOW(),
  "FechaModificacion" TIMESTAMP default NOW(),
  PRIMARY KEY ("IdOperario")
);

CREATE TABLE "Stock" 
(
  "IdStock"           int       NOT NULL,
  "CostoMedio"        float     NOT NULL,
  "Existencia"        boolean   NOT NULL,
  "ValorStock"        float     NOT NULL,
  "F.ul.ent"          date      NOT NULL,
  "F.ulsal"           date      ,
  "Cat"               varchar(50)  NOT NULL,
  "FkAlmacen"         int       NOT NULL,
  "FkArticulo"        int       NOT NULL,
  "FechaCreacion"     TIMESTAMP default NOW(),
  "FechaModificacion" TIMESTAMP default NOW(),
  PRIMARY KEY ("IdStock")
);

CREATE TABLE "OrdenesReparacion" 
(
  "IdOrdenReparacion"         int       NOT NULL,
  "ReferenciaOR"              varchar(250) NOT NULL, --
  -- "IDV"                       varchar(250) NOT NULL, --
  -- "Recep"                     varchar(50)  NOT NULL, --
  "FechaApertura"             date      NOT NULL, --
  "FechaCierre"               date      , --
  -- "FechaPrimera"           date      NOT NULL, --
  -- "FechaUltimo"            date      , --
  "TiempoFacturado"           float      , --
  "TiempoInvertido"           float      , --
  "Base"                      float     , --
  "ManoObra"                  float     , --
  "ManoObraSub"               float     , --
  "Recambio"                  float     , --
  "CostoManoObra"             float     , --
  "CostoSub"                  float     , --
  "CostoRecambio"             float     , --
  -- "NumeroLocal"                  varchar(50)  , --
  "FkCuentaCargo"             int       NOT NULL,
  "FkCuentaTitular"           int       NOT NULL,
  "FkTipoOrdenReparacion"     int       NOT NULL,
  "FkTaller"                  int       NOT NULL, --
  -- "FkCliente"                 int       NOT NULL,
  "FkVehiculo"                int       NOT NULL,
  "FechaCreacion"             TIMESTAMP default NOW(),
  "FechaModificacion"         TIMESTAMP default NOW(),
  PRIMARY KEY ("IdOrdenReparacion")
);

CREATE TABLE "OrdenesVentaMostrador" 
(
  "IdOrdenVentaMostrador" int       NOT NULL,
  "Referencia"            varchar      NOT NULL,
  "SerieNum"              int       NOT NULL,
  "Fecha"                 date      NOT NULL,
  "Canal"                 varchar(50)  NOT NULL,
  "Vende"                 varchar(100) NOT NULL,
  "Can"                   int       NOT NULL,
  "PVP"                   float     NOT NULL,
  "Dto"                   float     ,
  "Neto"                  float     NOT NULL,
  "Costo"                 float     NOT NULL,
  "FkCliente"             int       NOT NULL,
  "FkTipoVenta"           int       NOT NULL,
  "FkArticulo"            int       NOT NULL,
  "FkAlmacen"             int       NOT NULL,
  "FechaCreacion"         TIMESTAMP default NOW(),
  "FechaModificacion"     TIMESTAMP default NOW(),
  PRIMARY KEY ("IdOrdenVentaMostrador")
);

CREATE TABLE "OrdenesVentaTaller" 
(
  "IdOrdenVentaTaller"   int       NOT NULL,
  "Recep"                varchar(50)  NOT NULL,
  "TipoCliente"          varchar(50)  NOT NULL,
  "FechaSalida"          date      ,
  "FechaCierre"          date      ,
  "ClaveDto"             varchar(50)  NOT NULL,
  "Canti"                int       NOT NULL,
  "PVP"                  float     NOT NULL,
  "Dto"                  float     ,
  "Neto"                 float     NOT NULL,
  "Costo"                float     NOT NULL,
  "FkCliente"            int       NOT NULL,
  "FkTipoVenta"          int       NOT NULL,
  "FkArticulo"           int       NOT NULL,
  "FkOrdenReparacion"    int       NOT NULL,
  "FkAlmacen"            int       NOT NULL,
  "FechaCreacion"        TIMESTAMP default NOW(),
  "FechaModificacion"    TIMESTAMP default NOW(),
  PRIMARY KEY ("IdOrdenVentaTaller")
);

CREATE TABLE "Talleres" 
(
  "IdTaller"             int       NOT NULL,
  "Codigo"               int       NOT NULL,
  "Nombre"               varchar(50)  NOT NULL,
  "FkEmpresa"            int       NOT NULL,
  "FechaCreacion"        TIMESTAMP default NOW(),
  "FechaModificacion"    TIMESTAMP default NOW(),
  PRIMARY KEY ("IdTaller")
);

CREATE TABLE "TiposHoras" 
(
  "IdTipoHoras"          int       NOT NULL,
  "Codigo"               varchar(50)  NOT NULL,
  "Descripcion"          varchar(250) ,
  "FechaCreacion"        TIMESTAMP default NOW(),
  "FechaModificacion"    TIMESTAMP default NOW(),
  PRIMARY KEY ("IdTipoHoras")
);

CREATE TABLE "TiposOrdenesReparacion" 
(
  "IdTipoOrdenReparacion" int       NOT NULL,
  "Codigo"                varchar(50)  NOT NULL,
  "Descripcion"           varchar(250) ,
  "FechaCreacion"         TIMESTAMP default NOW(),
  "FechaModificacion"     TIMESTAMP default NOW(),
  PRIMARY KEY ("IdTipoOrdenReparacion")
);

CREATE TABLE "TiposVentasAlmacen" 
(
  "IdTipoVenta"          int       NOT NULL,
  "Codigo"               varchar(50)  NOT NULL,
  "Descripcion"          varchar(250) ,
  "FechaCreacion"        TIMESTAMP default NOW(),
  "FechaModificacion"    TIMESTAMP default NOW(),
  PRIMARY KEY ("IdTipoVenta")
);

CREATE TABLE "Vehiculos" 
(
  "IdVehiculo"           int       NOT NULL,
  "IDV"                  int       NOT NULL,
  "Matricula"            varchar(750),
  "Bastidor"             varchar(750)  NOT NULL,
  "Mar"                  varchar(750)  NOT NULL,
  "Modelo"               varchar(750)       ,
  "FechaMatriculacion"   date      ,
  "Kilometros"           bigint    ,
  "FechaUltimaVisita"    date      ,
  "Familia"              varchar(750)       ,
  "CodigoModelo"         varchar(750)  ,
  "FkCuentaTitular"      int       NOT NULL,
  "FkCuentaCliente"      int       NOT NULL,
  "FkCuentaConductor"    int       ,
  "FechaCreacion"        TIMESTAMP default NOW(),
  "FechaModificacion"    TIMESTAMP default NOW(),
  PRIMARY KEY ("IdVehiculo")
);


ALTER TABLE "BonosPresencia"
  ADD CONSTRAINT "FK_TipoHoras_TO_BonosPresencia"
    FOREIGN KEY ("FkTipoHoras")
    REFERENCES "TiposHoras" ("IdTipoHoras");

ALTER TABLE "BonosPresencia"
  ADD CONSTRAINT "FK_Talleres_TO_BonosPresencia"
    FOREIGN KEY ("FkTaller")
    REFERENCES "Talleres" ("IdTaller");

ALTER TABLE "BonosPresencia"
  ADD CONSTRAINT "FK_Operarios_TO_BonosPresencia"
    FOREIGN KEY ("FkOperario")
    REFERENCES "Operarios" ("IdOperario");


ALTER TABLE "Operarios"
  ADD CONSTRAINT "FK_Operarios_TO_Talleres"
    FOREIGN KEY ("FkTaller")
    REFERENCES "Talleres" ("IdTaller");


ALTER TABLE "Invertidas"
  ADD CONSTRAINT "FK_Operarios_TO_Invertidas"
    FOREIGN KEY ("FkOperario")
    REFERENCES "Operarios" ("IdOperario");

ALTER TABLE "Invertidas"
  ADD CONSTRAINT "FK_OrdenReparacion_TO_Invertidas"
    FOREIGN KEY ("FkOrdenReparacion")
    REFERENCES "OrdenesReparacion" ("IdOrdenReparacion");


ALTER TABLE "BonosTrabajadas"
  ADD CONSTRAINT "FK_Operarios_TO_BonosTrabajadas"
    FOREIGN KEY ("FkOperario")
    REFERENCES "Operarios" ("IdOperario");

ALTER TABLE "BonosTrabajadas"
  ADD CONSTRAINT "FK_OrdenReparacion_TO_BonosTrabajadas"
    FOREIGN KEY ("FkOrdenReparacion")
    REFERENCES "OrdenesReparacion" ("IdOrdenReparacion");


ALTER TABLE "OrdenesReparacion"
  ADD CONSTRAINT "FK_TipoOrdenesReparacion_TO_OrdenReparacion"
    FOREIGN KEY ("FkTipoOrdenReparacion")
    REFERENCES "TiposOrdenesReparacion" ("IdTipoOrdenReparacion");

ALTER TABLE "OrdenesReparacion"
  ADD CONSTRAINT "FK_Talleres_TO_OrdenReparacion"
    FOREIGN KEY ("FkTaller")
    REFERENCES "Talleres" ("IdTaller");

ALTER TABLE "OrdenesReparacion"
  ADD CONSTRAINT "FK_Vehiculo_TO_OrdenReparacion"
    FOREIGN KEY ("FkVehiculo")
    REFERENCES "Vehiculos" ("IdVehiculo");


ALTER TABLE "OrdenesReparacion"
  ADD CONSTRAINT "FK_Cliente_Cuenta_Cargo_TO_OrdenReparacion" 
  FOREIGN KEY ("FkCuentaCargo") 
  REFERENCES "Clientes" ("IdCliente");

ALTER TABLE "OrdenesReparacion"
  ADD CONSTRAINT "FK_Cliente_Cuenta_Titular_TO_OrdenReparacion" 
  FOREIGN KEY ("FkCuentaTitular")
  REFERENCES "Clientes" ("IdCliente");


ALTER TABLE "Vehiculos"
  ADD CONSTRAINT "FK_Cliente_TO_Vehiculo"
    FOREIGN KEY ("FkCuentaCliente")
    REFERENCES "Clientes" ("IdCliente");

ALTER TABLE "Vehiculos"
  ADD CONSTRAINT "FK_Cliente_CuentaTitular_TO_Vehiculo" 
  FOREIGN KEY ("FkCuentaTitular") 
  REFERENCES "Clientes" ("IdCliente");

ALTER TABLE "Vehiculos"
  ADD CONSTRAINT "FK_Cliente_CuentaConductor_TO_Vehiculo" 
  FOREIGN KEY ("FkCuentaConductor") 
  REFERENCES "Clientes" ("IdCliente");


ALTER TABLE "Stock"
  ADD CONSTRAINT "FK_Almacenes_TO_Stock"
    FOREIGN KEY ("FkAlmacen")
    REFERENCES "Almacenes" ("IdAlmacen");

ALTER TABLE "Stock"
  ADD CONSTRAINT "FK_Articulo_TO_Stock"
    FOREIGN KEY ("FkArticulo")
    REFERENCES "Articulos" ("IdArticulo");


ALTER TABLE "Almacenes"
  ADD CONSTRAINT "FK_Empresas_TO_Almacenes"
    FOREIGN KEY ("FkEmpresa")
    REFERENCES "Empresas" ("IdEmpresa");


ALTER TABLE "OrdenesVentaTaller"
  ADD CONSTRAINT "FK_TiposVentasAlmacen_TO_OrdenVentaTaller"
    FOREIGN KEY ("FkTipoVenta")
    REFERENCES "TiposVentasAlmacen" ("IdTipoVenta");

ALTER TABLE "OrdenesVentaTaller"
  ADD CONSTRAINT "FK_Cliente_TO_OrdenVentaTaller"
    FOREIGN KEY ("FkCliente")
    REFERENCES "Clientes" ("IdCliente");

ALTER TABLE "OrdenesVentaTaller"
  ADD CONSTRAINT "FK_Articulo_TO_OrdenVentaTaller"
    FOREIGN KEY ("FkArticulo")
    REFERENCES "Articulos" ("IdArticulo");

ALTER TABLE "OrdenesVentaTaller"
  ADD CONSTRAINT "FK_OrdenReparacion_TO_OrdenVentaTaller"
    FOREIGN KEY ("FkOrdenReparacion")
    REFERENCES "OrdenesReparacion" ("IdOrdenReparacion");

ALTER TABLE "OrdenesVentaTaller"
  ADD CONSTRAINT "FK_Almacenes_TO_OrdenVentaTaller"
    FOREIGN KEY ("FkAlmacen")
    REFERENCES "Almacenes" ("IdAlmacen");


ALTER TABLE "Compras"
  ADD CONSTRAINT "FK_Almacenes_TO_Compras"
    FOREIGN KEY ("FkAlmacen")
    REFERENCES "Almacenes" ("IdAlmacen");

ALTER TABLE "Compras"
  ADD CONSTRAINT "FK_Cuentas_TO_Compras"
    FOREIGN KEY ("FkCuenta")
    REFERENCES "Clientes" ("IdCliente");

ALTER TABLE "Compras"
  ADD CONSTRAINT "FK_Articulo_TO_Compras"
    FOREIGN KEY ("FkArticulo")
    REFERENCES "Articulos" ("IdArticulo");


ALTER TABLE "OrdenesVentaMostrador"
  ADD CONSTRAINT "FK_TiposVentasAlmacen_TO_OrdenVentaMostrador"
    FOREIGN KEY ("FkTipoVenta")
    REFERENCES "TiposVentasAlmacen" ("IdTipoVenta");

ALTER TABLE "OrdenesVentaMostrador"
  ADD CONSTRAINT "FK_Articulo_TO_OrdenVentaMostrador"
    FOREIGN KEY ("FkArticulo")
    REFERENCES "Articulos" ("IdArticulo");

ALTER TABLE "OrdenesVentaMostrador"
  ADD CONSTRAINT "FK_Cliente_TO_OrdenVentaMostrador"
    FOREIGN KEY ("FkCliente")
    REFERENCES "Clientes" ("IdCliente");

ALTER TABLE "OrdenesVentaMostrador"
  ADD CONSTRAINT "FK_Almacenes_TO_OrdenVentaMostrador"
    FOREIGN KEY ("FkAlmacen")
    REFERENCES "Almacenes" ("IdAlmacen");
    

ALTER TABLE "Talleres"
  ADD CONSTRAINT "FK_Empresas_TO_Talleres"
    FOREIGN KEY ("FkEmpresa")
    REFERENCES "Empresas" ("IdEmpresa");

ALTER TABLE "Articulos"
  ADD CONSTRAINT "FK_ALmacenes_TO_Artculos"
    FOREIGN KEY ("FkAlmacen")
    REFERENCES "Almacenes" ("IdAlmacen")

