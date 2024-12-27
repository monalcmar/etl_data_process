-- DROP SCHEMA gold;

CREATE SCHEMA gold AUTHORIZATION postgres;
-- gold."Articulos" definition

-- Drop table

-- DROP TABLE gold."Articulos";

CREATE TABLE gold."Articulos" (
	"IdArticulo" int4 NOT NULL,
	"Mar" int4 NOT NULL,
	"Referencia" bpchar(50) NOT NULL,
	"Articulo" bpchar(50) NOT NULL,
	"Denominacion" bpchar(50) NOT NULL,
	"Familia" bpchar(50) NOT NULL,
	"PVP" float8 NOT NULL,
	"ClaveDTO" bpchar(50) NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	"FechaAlta" timestamp NULL,
	CONSTRAINT "Articulos_pkey" PRIMARY KEY ("IdArticulo")
);


-- gold."Clientes" definition

-- Drop table

-- DROP TABLE gold."Clientes";

CREATE TABLE gold."Clientes" (
	"IdCliente" int4 NOT NULL,
	"Codigo" bpchar(50) NOT NULL,
	"Categoria" bpchar(50) NOT NULL,
	"Nombre" bpchar(50) NOT NULL,
	"DNI/CIF" bpchar(50) NULL,
	"Direccion" bpchar(250) NULL,
	"CodigoPostal" bpchar(50) NULL,
	"Localidad" bpchar(50) NULL,
	"CorreoElectronico" bpchar(100) NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Clientes_pkey" PRIMARY KEY ("IdCliente")
);


-- gold."Empresas" definition

-- Drop table

-- DROP TABLE gold."Empresas";

CREATE TABLE gold."Empresas" (
	"IdEmpresa" int4 NOT NULL,
	"Codigo" int4 NOT NULL,
	"Nombre" bpchar(50) NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Empresas_pkey" PRIMARY KEY ("IdEmpresa")
);


-- gold."TiposHoras" definition

-- Drop table

-- DROP TABLE gold."TiposHoras";

CREATE TABLE gold."TiposHoras" (
	"IdTipoHoras" int4 NOT NULL,
	"Codigo" bpchar(50) NOT NULL,
	"Descripcion" bpchar(250) NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "TiposHoras_pkey" PRIMARY KEY ("IdTipoHoras")
);


-- gold."TiposOrdenesReparacion" definition

-- Drop table

-- DROP TABLE gold."TiposOrdenesReparacion";

CREATE TABLE gold."TiposOrdenesReparacion" (
	"IdTipoOrdenReparacion" int4 NOT NULL,
	"Codigo" bpchar(50) NOT NULL,
	"Descripcion" bpchar(250) NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "TiposOrdenesReparacion_pkey" PRIMARY KEY ("IdTipoOrdenReparacion")
);


-- gold."TiposVentasAlmacen" definition

-- Drop table

-- DROP TABLE gold."TiposVentasAlmacen";

CREATE TABLE gold."TiposVentasAlmacen" (
	"IdTipoVenta" int4 NOT NULL,
	"Codigo" bpchar(50) NOT NULL,
	"Descripcion" bpchar(250) NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "TiposVentasAlmacen_pkey" PRIMARY KEY ("IdTipoVenta")
);


-- gold."Almacenes" definition

-- Drop table

-- DROP TABLE gold."Almacenes";

CREATE TABLE gold."Almacenes" (
	"IdAlmacen" int4 NOT NULL,
	"Codigo" int4 NOT NULL,
	"Nombre" bpchar(50) NOT NULL,
	"FkEmpresa" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Almacenes_pkey" PRIMARY KEY ("IdAlmacen"),
	CONSTRAINT "FK_Empresas_TO_Almacenes" FOREIGN KEY ("FkEmpresa") REFERENCES gold."Empresas"("IdEmpresa")
);


-- gold."Compras" definition

-- Drop table

-- DROP TABLE gold."Compras";

CREATE TABLE gold."Compras" (
	"IdCompra" int4 NOT NULL,
	"Fecha" date NOT NULL,
	"ReferenciaCompra" bpchar(250) NOT NULL,
	"NombreProvedor" bpchar(100) NOT NULL,
	"T.Com" float8 NOT NULL,
	"Albaran" bpchar(100) NOT NULL,
	"Cantidad" int4 NOT NULL,
	"P.Compra" float8 NOT NULL,
	"TotalCompra" float8 NOT NULL,
	"PVP" float8 NOT NULL,
	"FkCuenta" int4 NOT NULL,
	"FkAlmacen" int4 NOT NULL,
	"FkCliente" int4 NOT NULL,
	"FkArticulo" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Compras_pkey" PRIMARY KEY ("IdCompra"),
	CONSTRAINT "FK_Almacenes_TO_Compras" FOREIGN KEY ("FkAlmacen") REFERENCES gold."Almacenes"("IdAlmacen"),
	CONSTRAINT "FK_Articulo_TO_Compras" FOREIGN KEY ("FkArticulo") REFERENCES gold."Articulos"("IdArticulo"),
	CONSTRAINT "FK_Cliente_TO_Compras" FOREIGN KEY ("FkCliente") REFERENCES gold."Clientes"("IdCliente")
);


-- gold."OrdenesVentaMostrador" definition

-- Drop table

-- DROP TABLE gold."OrdenesVentaMostrador";

CREATE TABLE gold."OrdenesVentaMostrador" (
	"IdOrdenVentaMostrador" int4 NOT NULL,
	"Referencia" bpchar(1) NOT NULL,
	"SerieNum" int4 NOT NULL,
	"Fecha" date NOT NULL,
	"Canal" bpchar(50) NOT NULL,
	"Vende" bpchar(100) NOT NULL,
	"Can" int4 NOT NULL,
	"PVP" float8 NOT NULL,
	"Dto" float8 NULL,
	"Neto" float8 NOT NULL,
	"Costo" float8 NOT NULL,
	"FkCliente" int4 NOT NULL,
	"FkTipoVenta" int4 NOT NULL,
	"FkArticulo" int4 NOT NULL,
	"FkAlmacen" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "OrdenesVentaMostrador_pkey" PRIMARY KEY ("IdOrdenVentaMostrador"),
	CONSTRAINT "FK_Almacenes_TO_OrdenVentaMostrador" FOREIGN KEY ("FkAlmacen") REFERENCES gold."Almacenes"("IdAlmacen"),
	CONSTRAINT "FK_Articulo_TO_OrdenVentaMostrador" FOREIGN KEY ("FkArticulo") REFERENCES gold."Articulos"("IdArticulo"),
	CONSTRAINT "FK_Cliente_TO_OrdenVentaMostrador" FOREIGN KEY ("FkCliente") REFERENCES gold."Clientes"("IdCliente"),
	CONSTRAINT "FK_TiposVentasAlmacen_TO_OrdenVentaMostrador" FOREIGN KEY ("FkTipoVenta") REFERENCES gold."TiposVentasAlmacen"("IdTipoVenta")
);


-- gold."Stock" definition

-- Drop table

-- DROP TABLE gold."Stock";

CREATE TABLE gold."Stock" (
	"IdStock" int4 NOT NULL,
	"CostoMedio" float8 NOT NULL,
	"Existencia" bool NOT NULL,
	"ValorStock" float8 NOT NULL,
	"F.ul.ent" date NOT NULL,
	"F.ulsal" date NULL,
	"Cat" bpchar(50) NOT NULL,
	"FkAlmacen" int4 NOT NULL,
	"FkArticulo" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Stock_pkey" PRIMARY KEY ("IdStock"),
	CONSTRAINT "FK_Almacenes_TO_Stock" FOREIGN KEY ("FkAlmacen") REFERENCES gold."Almacenes"("IdAlmacen"),
	CONSTRAINT "FK_Articulo_TO_Stock" FOREIGN KEY ("FkArticulo") REFERENCES gold."Articulos"("IdArticulo")
);


-- gold."Talleres" definition

-- Drop table

-- DROP TABLE gold."Talleres";

CREATE TABLE gold."Talleres" (
	"IdTaller" int4 NOT NULL,
	"Codigo" int4 NOT NULL,
	"Nombre" bpchar(50) NOT NULL,
	"FkEmpresa" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Talleres_pkey" PRIMARY KEY ("IdTaller"),
	CONSTRAINT "FK_Empresas_TO_Talleres" FOREIGN KEY ("FkEmpresa") REFERENCES gold."Empresas"("IdEmpresa")
);


-- gold."Vehiculos" definition

-- Drop table

-- DROP TABLE gold."Vehiculos";

CREATE TABLE gold."Vehiculos" (
	"IdVehiculo" int4 NOT NULL,
	"IDV" int4 NOT NULL,
	"Matricula" bpchar(50) NOT NULL,
	"Bastidor" bpchar(50) NOT NULL,
	"Mar" bpchar(50) NOT NULL,
	"Modelo" int4 NOT NULL,
	"FechaMatriculacion" date NULL,
	"Kilometros" int4 NULL,
	"FechaUltimaVisita" date NOT NULL,
	"Familia" int4 NULL,
	"CodigoModelo" bpchar(50) NULL,
	"FkCuentaTitular" int4 NOT NULL,
	"FkCuentaCliente" int4 NOT NULL,
	"FkCuentaConductor" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Vehiculos_pkey" PRIMARY KEY ("IdVehiculo"),
	CONSTRAINT "FK_Cliente_TO_Vehiculo" FOREIGN KEY ("FkCuentaCliente") REFERENCES gold."Clientes"("IdCliente"),
	CONSTRAINT vehiculos_clientes_fk FOREIGN KEY ("FkCuentaTitular") REFERENCES gold."Clientes"("IdCliente"),
	CONSTRAINT vehiculos_clientes_fk_1 FOREIGN KEY ("FkCuentaConductor") REFERENCES gold."Clientes"("IdCliente")
);


-- gold."Operarios" definition

-- Drop table

-- DROP TABLE gold."Operarios";

CREATE TABLE gold."Operarios" (
	"IdOperario" int4 NOT NULL,
	"Codigo" bpchar(50) NOT NULL,
	"Nombre" bpchar(50) NOT NULL,
	"Seccion" bpchar(50) NOT NULL,
	"Activo" bpchar(50) NOT NULL,
	"FkTaller" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Operarios_pkey" PRIMARY KEY ("IdOperario"),
	CONSTRAINT "FK_Talleres_TO_Operarios" FOREIGN KEY ("FkTaller") REFERENCES gold."Talleres"("IdTaller")
);


-- gold."OrdenesReparacion" definition

-- Drop table

-- DROP TABLE gold."OrdenesReparacion";

CREATE TABLE gold."OrdenesReparacion" (
	"IdOrdenReparacion" int4 NOT NULL,
	"Referencia" bpchar(250) NOT NULL,
	"IDV" bpchar(250) NOT NULL,
	"Recep" bpchar(50) NOT NULL,
	"FechaApertura" date NOT NULL,
	"FechaCierre" date NULL,
	"FechaPrimero" date NOT NULL,
	"FechaUltimo" date NULL,
	"TiempoFac" time NULL,
	"TiempoInvertido" time NULL,
	"Base" float8 NULL,
	"ManoObra" float8 NULL,
	"MoSub" float8 NULL,
	"Recamb" float8 NULL,
	"CostoMo" float8 NULL,
	"CostoSub" float8 NULL,
	"CostoRec" float8 NULL,
	"NroLocal" bpchar(50) NULL,
	"FkCliente Cuenta Cargo" int4 NOT NULL,
	"FkCliente Cuenta Titular" int4 NOT NULL,
	"FkTipoOrdenReparacion" int4 NOT NULL,
	"FkTaller" int4 NOT NULL,
	"FkCliente" int4 NOT NULL,
	"FkVehiculo" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "OrdenesReparacion_pkey" PRIMARY KEY ("IdOrdenReparacion"),
	CONSTRAINT "FK_Cliente_TO_OrdenReparacion" FOREIGN KEY ("FkCliente") REFERENCES gold."Clientes"("IdCliente"),
	CONSTRAINT "FK_Talleres_TO_OrdenReparacion" FOREIGN KEY ("FkTaller") REFERENCES gold."Talleres"("IdTaller"),
	CONSTRAINT "FK_TipoOrdenesReparacion_TO_OrdenReparacion" FOREIGN KEY ("FkTipoOrdenReparacion") REFERENCES gold."TiposOrdenesReparacion"("IdTipoOrdenReparacion"),
	CONSTRAINT "FK_Vehiculo_TO_OrdenReparacion" FOREIGN KEY ("FkVehiculo") REFERENCES gold."Vehiculos"("IdVehiculo"),
	CONSTRAINT ordenesreparacion_clientes_fk FOREIGN KEY ("FkCliente Cuenta Cargo") REFERENCES gold."Clientes"("IdCliente"),
	CONSTRAINT ordenesreparacion_clientes_fk_1 FOREIGN KEY ("FkCliente Cuenta Titular") REFERENCES gold."Clientes"("IdCliente")
);


-- gold."OrdenesVentaTaller" definition

-- Drop table

-- DROP TABLE gold."OrdenesVentaTaller";

CREATE TABLE gold."OrdenesVentaTaller" (
	"IdOrdenVentaTaller" int4 NOT NULL,
	"Recep" bpchar(50) NOT NULL,
	"TipoCliente" bpchar(50) NOT NULL,
	"FechaSalida" date NULL,
	"FechaCierre" date NULL,
	"ClaveDto" bpchar(50) NOT NULL,
	"Canti" int4 NOT NULL,
	"PVP" float8 NOT NULL,
	"Dto" float8 NULL,
	"Neto" float8 NOT NULL,
	"Costo" float8 NOT NULL,
	"FkCliente" int4 NOT NULL,
	"FkTipoVenta" int4 NOT NULL,
	"FkArticulo" int4 NOT NULL,
	"FkOrdenReparacion" int4 NOT NULL,
	"FkAlmacen" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "OrdenesVentaTaller_pkey" PRIMARY KEY ("IdOrdenVentaTaller"),
	CONSTRAINT "FK_Almacenes_TO_OrdenVentaTaller" FOREIGN KEY ("FkAlmacen") REFERENCES gold."Almacenes"("IdAlmacen"),
	CONSTRAINT "FK_Articulo_TO_OrdenVentaTaller" FOREIGN KEY ("FkArticulo") REFERENCES gold."Articulos"("IdArticulo"),
	CONSTRAINT "FK_Cliente_TO_OrdenVentaTaller" FOREIGN KEY ("FkCliente") REFERENCES gold."Clientes"("IdCliente"),
	CONSTRAINT "FK_OrdenReparacion_TO_OrdenVentaTaller" FOREIGN KEY ("FkOrdenReparacion") REFERENCES gold."OrdenesReparacion"("IdOrdenReparacion"),
	CONSTRAINT "FK_TiposVentasAlmacen_TO_OrdenVentaTaller" FOREIGN KEY ("FkTipoVenta") REFERENCES gold."TiposVentasAlmacen"("IdTipoVenta")
);


-- gold."BonosPresencia" definition

-- Drop table

-- DROP TABLE gold."BonosPresencia";

CREATE TABLE gold."BonosPresencia" (
	"IdBonoPresencia" int4 NOT NULL,
	"Fecha" date NOT NULL,
	"EntradaPresencia" time NOT NULL,
	"SalidaPresencia" time NULL,
	"DiferenciaPresencia" float8 NULL,
	"FkTipoHoras" int4 NOT NULL,
	"FkTaller" int4 NOT NULL,
	"FkOperario" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "BonosPresencia_pkey" PRIMARY KEY ("IdBonoPresencia"),
	CONSTRAINT "FK_Operarios_TO_BonosPresencia" FOREIGN KEY ("FkOperario") REFERENCES gold."Operarios"("IdOperario"),
	CONSTRAINT "FK_Talleres_TO_BonosPresencia" FOREIGN KEY ("FkTaller") REFERENCES gold."Talleres"("IdTaller"),
	CONSTRAINT "FK_TipoHoras_TO_BonosPresencia" FOREIGN KEY ("FkTipoHoras") REFERENCES gold."TiposHoras"("IdTipoHoras")
);


-- gold."BonosTrabajadas" definition

-- Drop table

-- DROP TABLE gold."BonosTrabajadas";

CREATE TABLE gold."BonosTrabajadas" (
	"IdBonoTrabajadas" int4 NOT NULL,
	"Fecha" date NOT NULL,
	"Entrada" time NOT NULL,
	"Salida" time NULL,
	"FkOperario" int4 NOT NULL,
	"FkOrdenReparacion" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "BonosTrabajadas_pkey" PRIMARY KEY ("IdBonoTrabajadas"),
	CONSTRAINT "FK_Operarios_TO_BonosTrabajadas" FOREIGN KEY ("FkOperario") REFERENCES gold."Operarios"("IdOperario"),
	CONSTRAINT "FK_OrdenReparacion_TO_BonosTrabajadas" FOREIGN KEY ("FkOrdenReparacion") REFERENCES gold."OrdenesReparacion"("IdOrdenReparacion")
);


-- gold."Invertidas" definition

-- Drop table

-- DROP TABLE gold."Invertidas";

CREATE TABLE gold."Invertidas" (
	"IdBonoInvertidas" int4 NOT NULL,
	"FechaApertura" date NOT NULL,
	"FechaCierra" date NULL,
	"TipoFactura" bpchar(50) NOT NULL,
	"Recep" bpchar(50) NOT NULL,
	"TiempoAsignado" float8 NULL,
	"TiempoInvertido" float8 NULL,
	"FkOperario" int4 NOT NULL,
	"FkOrdenReparacion" int4 NOT NULL,
	"FechaCreacion" timestamp DEFAULT now() NULL,
	"FechaModificacion" timestamp DEFAULT now() NULL,
	CONSTRAINT "Invertidas_pkey" PRIMARY KEY ("IdBonoInvertidas"),
	CONSTRAINT "FK_Operarios_TO_Invertidas" FOREIGN KEY ("FkOperario") REFERENCES gold."Operarios"("IdOperario"),
	CONSTRAINT "FK_OrdenReparacion_TO_Invertidas" FOREIGN KEY ("FkOrdenReparacion") REFERENCES gold."OrdenesReparacion"("IdOrdenReparacion")
);



-- DROP FUNCTION gold.update_fecha_modificacion();

CREATE OR REPLACE FUNCTION gold.update_fecha_modificacion()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
BEGIN
    NEW."FechaModificacion" = NOW();
    RETURN NEW;
END;
$function$
;