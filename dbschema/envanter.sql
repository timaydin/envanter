CREATE SCHEMA IF NOT EXISTS "public";

CREATE  TABLE "public".categories ( 
	id                   serial  NOT NULL  ,
	name                 varchar(100)  NOT NULL  ,
	description          varchar(500)    ,
	parent_id            integer    ,
	CONSTRAINT pk_categories PRIMARY KEY ( id )
 );

CREATE  TABLE "public".document_types ( 
	id                   serial  NOT NULL  ,
	name                 varchar(100)  NOT NULL  ,
	CONSTRAINT pk_data_types PRIMARY KEY ( id )
 );

CREATE  TABLE "public".documents ( 
	id                   serial    ,
	name                 varchar(100)  NOT NULL  ,
	description          varchar(500)    ,
	document_type_id     integer  NOT NULL  ,
	document_path        varchar(500)  NOT NULL  ,
	CONSTRAINT unq_documents_id UNIQUE ( id ) 
 );

CREATE  TABLE "public".location_types ( 
	id                   serial  NOT NULL  ,
	name                 varchar(100)  NOT NULL  ,
	CONSTRAINT pk_location_types PRIMARY KEY ( id )
 );

CREATE  TABLE "public".locations ( 
	id                   serial  NOT NULL  ,
	name                 varchar(100)  NOT NULL  ,
	location_type_id     integer  NOT NULL  ,
	parent_id            integer    ,
	CONSTRAINT pk_locations PRIMARY KEY ( id )
 );

CREATE  TABLE "public".manufacturers ( 
	id                   serial  NOT NULL  ,
	name                 varchar(100)  NOT NULL  ,
	CONSTRAINT pk_manufacturers PRIMARY KEY ( id )
 );

CREATE  TABLE "public".packages ( 
	id                   serial  NOT NULL  ,
	name                 varchar(100)  NOT NULL  ,
	CONSTRAINT pk_packages PRIMARY KEY ( id )
 );

CREATE  TABLE "public".suppliers ( 
	id                   serial  NOT NULL  ,
	name                 varchar(100)  NOT NULL  ,
	CONSTRAINT pk_suppliers PRIMARY KEY ( id )
 );

CREATE  TABLE "public".components ( 
	id                   serial  NOT NULL  ,
	model                varchar(100)  NOT NULL  ,
	description          varchar(500)    ,
	manufacturer_id      integer    ,
	category_id          integer    ,
	package_id           integer    ,
	location_id          integer    ,
	stock                integer DEFAULT 0   ,
	CONSTRAINT pk_components PRIMARY KEY ( id )
 );

CREATE INDEX idx_components ON "public".components  ( model );

CREATE  TABLE "public".purchases ( 
	id                   serial  NOT NULL  ,
	"date"               date  NOT NULL  ,
	supplier_id          integer  NOT NULL  ,
	CONSTRAINT pk_purchases PRIMARY KEY ( id )
 );

CREATE  TABLE "public".component_document_links ( 
	id                   serial  NOT NULL  ,
	document_id          integer  NOT NULL  ,
	component_id         integer  NOT NULL  ,
	CONSTRAINT pk_component_document_links PRIMARY KEY ( id )
 );

CREATE  TABLE "public".purchase_details ( 
	id                   serial  NOT NULL  ,
	purchase_id          integer  NOT NULL  ,
	component_id         integer  NOT NULL  ,
	quantity             integer  NOT NULL  ,
	cost                 numeric    ,
	total_cost           numeric    ,
	CONSTRAINT pk_purchase_details PRIMARY KEY ( id )
 );

ALTER TABLE "public".component_document_links ADD CONSTRAINT fk_component_document_links_documents FOREIGN KEY ( document_id ) REFERENCES "public".documents( id );

ALTER TABLE "public".component_document_links ADD CONSTRAINT fk_component_document_links_components FOREIGN KEY ( component_id ) REFERENCES "public".components( id );

ALTER TABLE "public".components ADD CONSTRAINT fk_components_locations FOREIGN KEY ( location_id ) REFERENCES "public".locations( id );

ALTER TABLE "public".components ADD CONSTRAINT fk_components_categories FOREIGN KEY ( category_id ) REFERENCES "public".categories( id );

ALTER TABLE "public".components ADD CONSTRAINT fk_components_packages FOREIGN KEY ( package_id ) REFERENCES "public".packages( id );

ALTER TABLE "public".components ADD CONSTRAINT fk_components_manufacturers FOREIGN KEY ( manufacturer_id ) REFERENCES "public".manufacturers( id );

ALTER TABLE "public".documents ADD CONSTRAINT fk_documents_document_types FOREIGN KEY ( document_type_id ) REFERENCES "public".document_types( id );

ALTER TABLE "public".locations ADD CONSTRAINT fk_locations_location_types FOREIGN KEY ( location_type_id ) REFERENCES "public".location_types( id );

ALTER TABLE "public".purchase_details ADD CONSTRAINT fk_purchase_details_purchases FOREIGN KEY ( purchase_id ) REFERENCES "public".purchases( id );

ALTER TABLE "public".purchase_details ADD CONSTRAINT fk_purchase_details_components FOREIGN KEY ( component_id ) REFERENCES "public".components( id );

ALTER TABLE "public".purchases ADD CONSTRAINT fk_purchases_suppliers FOREIGN KEY ( supplier_id ) REFERENCES "public".suppliers( id );
