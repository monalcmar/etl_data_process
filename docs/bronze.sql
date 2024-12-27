DROP TABLE IF EXISTS "U6321303_Almacenes";
DROP TABLE IF EXISTS "U6301303_Articulos";
DROP TABLE IF EXISTS "U551_Presencia";
DROP TABLE IF EXISTS "U532_Trabajadas";
DROP TABLE IF EXISTS "U6301303_Clientes";
DROP TABLE IF EXISTS "U553_Compras";
DROP TABLE IF EXISTS "U6311303_Empresas";
DROP TABLE IF EXISTS "U555_Invertidas";
DROP TABLE IF EXISTS "U6331303_Operarios";
DROP TABLE IF EXISTS "U552_Stock";
DROP TABLE IF EXISTS "U533_OrdenesReparacion";
DROP TABLE IF EXISTS "U554_VentasMostrador";
DROP TABLE IF EXISTS "U560_VentasTaller";
DROP TABLE IF EXISTS "U6311303_Talleres";
DROP TABLE IF EXISTS "ULSTTHPT_TiposHoras";
DROP TABLE IF EXISTS "UU2_TiposOrdenes";
DROP TABLE IF EXISTS "ULSTTVPT_TiposVentas";
DROP TABLE IF EXISTS "U6341303_Vehiculos";

-- Create tables
CREATE TABLE "U6321303_Almacenes" (
  "Codi"   TEXT,
  "Nombre" TEXT,
  "Empre"  TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U6301303_Articulos" (
  "Mar"          TEXT,
  "Ref.articulo" TEXT,
  "Articulo"     TEXT,
  "Denominacion" TEXT,
  "Alma"         TEXT,
  "Famil"        TEXT,
  "P.V.P."       TEXT,
  "Clave DTO"    TEXT,
  "F.alta"       TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U551_Presencia" (
  "Tall"            TEXT,
  "Fecha"           TEXT,
  "Secc"            TEXT,
  "Operario"        TEXT,
  "NOMBRE OPERARIO" TEXT,
  "ENTRADA PRES"    TEXT,
  "SALIDA PRESE"    TEXT,
  "DIF.PRES"       	TEXT,
  "Tipo h"          TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U532_Trabajadas" (
  "Tall"            TEXT,
  "Fecha"           TEXT,
  "Secc"            TEXT,
  "Operario"        TEXT,
  "NOMBRE OPERARIO" TEXT,
  "Ref.OR"          TEXT,
  "Tipo O.R."       TEXT,
  "IDV"             TEXT,
  "Matricula"       TEXT,
  "Entra"         	TEXT,
  "Salid"           TEXT,
  "DIF TRAB"        TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U6301303_Clientes" (
  "Codigo cuenta"  TEXT,
  "Cat"            TEXT,
  "Nombre cliente" TEXT,
  "DNI/CIF"        TEXT,
  "Dirección"      TEXT,
  "C.P."           TEXT,
  "Localidad"      TEXT,
  "E-mail"         TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U553_Compras" (
  "Alma"          	 TEXT,
  "Fecha"            TEXT,
  "Referenci"        TEXT,
  "Cuenta"           TEXT,
  "Nombre proveedor" TEXT,
  "T.com"            TEXT,
  "Albaran"          TEXT,
  "Artículo"         TEXT,
  "Mar"              TEXT,
  "Artículo.1"		   TEXT,
  "Denominacion"     TEXT,
  "Clave"            TEXT,
  "Famil"            TEXT,
  "Fam.apro"         TEXT,
  "F.Market"         TEXT,
  "Canti"            TEXT,
  "P.compra"         TEXT,
  "Tot.compra"       TEXT,
  "P.V.P."           TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U6311303_Empresas" (
  "Codig" 				TEXT,
  "Nombre" 				TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U555_Invertidas" (
  "Tall"        TEXT,
  "REF.OR"      TEXT,
  "Fec.apertu"  TEXT,
  "F.cierre"    TEXT,
  "Matricula"   TEXT,
  "Cta.cargo"  	TEXT,
  "Tipo O.R."   TEXT,
  "Tipo fac"    TEXT,
  "Recep"       TEXT,
  "Operario"	  TEXT,
  "Tiempo asig" TEXT,
  "T.INVERT."   TEXT,
  "Bastidor"    TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U6331303_Operarios" (
  "Codigo" TEXT,
  "Nombre" TEXT,
  "Sec"    TEXT,
  "Tall"   TEXT,
  "Act"    TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U552_Stock" (
  "Alma"         TEXT,
  "Artículo"     TEXT,
  "Mar"          TEXT,
  "Ref.articulo" TEXT,
  "Descripción"  TEXT,
  "Gru"          TEXT,
  "Famil"        TEXT,
  "Fam.apro"     TEXT,
  "F.Marketin"   TEXT,
  "CLAVE DTO"    TEXT,
  "P.V.P."       TEXT,
  "Costo medi"   TEXT,
  "Exist."       TEXT,
  "Valor stock"  TEXT,
  "F.ul.ent"     TEXT,
  "F.ul.sal"     TEXT,
  "Cat"          TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U533_OrdenesReparacion" (
  "Tall"           TEXT,
  "REF.OR"         TEXT,
  "IDV"            TEXT,
  "Matricula"      TEXT,
  "Cta.cargo"      TEXT,
  "Nombre cliente" TEXT,
  "DNI/CIF"        TEXT,
  "C.P."           TEXT,
  "Marca"          TEXT,
  "Tipo O.R."      TEXT,
  "Recep"          TEXT,
  "Fec.apertu"     TEXT,
  "Hora.cre"       TEXT,
  "F.cierre"       TEXT,
  "HORA."          TEXT,
  "Fec.prim"       TEXT,
  "Fec.ult."       TEXT,
  "Tiem.fac"       TEXT,
  "T.INVERT."      TEXT,
  "DIF.F-I"        TEXT,
  "Base"           TEXT,
  "Mano obra"      TEXT,
  "MO.SUB"         TEXT,
  "Recamb."        TEXT,
  "COSTO MO"       TEXT,
  "COSTO SUB"      TEXT,
  "Costo rec"      TEXT,
  "Nro.local."     TEXT,
  "Est"            TEXT,
  "Serie/num"      TEXT,
  "Bastidor"       TEXT,
  "Cta. tit"       TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U554_VentasMostrador" (
  "Alma"                TEXT,
  "Refer."              TEXT,
  "Serie/num"           TEXT,
  "Fecha"               TEXT,
  "Cuenta"              TEXT,
  "Nombre cliente"      TEXT,
  "DNI/CIF"             TEXT,
  "C.P."                TEXT,
  "Tipo de cl"          TEXT,
  "canal"               TEXT,
  "Vende"               TEXT,
  "Tipo venta"          TEXT,
  "Marca"               TEXT,
  "Artículo"            TEXT,
  "Denominacion"        TEXT,
  "Fam.apro"            TEXT,
  "F.Marketin"          TEXT,
  "Familia"             TEXT,
  "Grupo"               TEXT,
  "Can"                 TEXT,
  "P.V.P."              TEXT,
  "Dto."                TEXT,
  "Neto"                TEXT,
  "Costo"               TEXT,
  "% Ben"               TEXT,
  "Beneficio"           TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U560_VentasTaller" (
  "Alma"                TEXT,
  "Refer."              TEXT,
  "Tipo venta"          TEXT,
  "Recep"               TEXT,
  "Tipo clien"          TEXT,
  "Cuenta"              TEXT,
  "Nombre cliente"      TEXT,
  "DNI/CIF"             TEXT,
  "C.P."                TEXT,
  "Fec.sali"            TEXT,
  "F.cierre"            TEXT,
  "Artículo"            TEXT,
  "Denominacion"        TEXT,
  "Famil"               TEXT,
  "Fam.a"               TEXT,
  "F.Marketing"         TEXT,
  "Grupo"               TEXT,
  "CLAVE DTO "          TEXT,
  "Canti"               TEXT,
  "P.V.P."              TEXT,
  "Dto."                TEXT,
  "Neto"                TEXT,
  "Costo"               TEXT,
  "Beneficio"           TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U6311303_Talleres" (
  "Codig"               TEXT,
  "Nombre"              TEXT,
  "Empre"               TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "ULSTTHPT_TiposHoras" (
  "Codigo"              TEXT,
  "Descripcion"         TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "UU2_TiposOrdenes" (
  "Codigo"              TEXT,
  "Descripcion"         TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "ULSTTVPT_TiposVentas" (
  "Codigo"              TEXT,
  "Descripcion"         TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);

CREATE TABLE "U6341303_Vehiculos" (
  "IDV"                 TEXT,
  "Matrícula"           TEXT,
  "Bastidor"            TEXT,
  "Mar"                 TEXT,
  "Modelo"              TEXT,
  "Cta Titul"           TEXT,
  "Cta. cli"            TEXT,
  "Cta. condu"          TEXT,
  "F. matri"            TEXT,
  "KM"                  TEXT,
  "F. últ. "            TEXT,
  "Famil"               TEXT,
  "Cód. modelo"         TEXT,
  "FechaCreacion" 		  TIMESTAMP default NOW(),
  "FechaModificacion" 	TIMESTAMP default NOW()
);



