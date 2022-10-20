CREATE TABLE pokemones(
  id NUMBER(7) PRIMARY KEY,
  nombre VARCHAR2(20) NOT NULL,
  numero NUMBER(3) NOT NULL,
  peso FLOAT NOT NULL,
  talla FLOAT NOT NULL,
  imagen VARCHAR(85),
  generacion_id NUMBER(2) not null
);

ALTER TABLE pokemones ADD (
  CONSTRAINT pokemones_pk PRIMARY KEY (id));

CREATE SEQUENCE pokemones_seq START WITH 1;

CREATE OR REPLACE TRIGGER pokemones_pk 
BEFORE INSERT ON pokemones 
FOR EACH ROW

BEGIN
  SELECT pokemones_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/