-- up
CREATE TABLE generaciones(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(20)
);

ALTER TABLE generaciones ADD (
  CONSTRAINT generaciones_pk PRIMARY KEY (ID));

CREATE SEQUENCE generaciones_seq START WITH 1;

CREATE OR REPLACE TRIGGER generaciones_pk 
BEFORE INSERT ON generaciones 
FOR EACH ROW

BEGIN
  SELECT generaciones_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/

-- down

DROP SEQUENCE generaciones_seq;
DROP TABLE generaciones;