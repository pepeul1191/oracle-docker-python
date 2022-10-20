CREATE TABLE pokemones_tipos(
  ID NUMBER(7) PRIMARY KEY,
  TIPO_ID NUMBER(7),
  POKEMON_ID NUMBER(7),
  FOREIGN KEY (TIPO_ID) REFERENCES TIPOS,
  FOREIGN KEY (POKEMON_ID) REFERENCES POKEMONES
);

ALTER TABLE pokemones_tipos ADD (
  CONSTRAINT pokemones_tipos_pk PRIMARY KEY (ID));

CREATE SEQUENCE pokemones_tipos_seq START WITH 1;

CREATE OR REPLACE TRIGGER pokemones_tipos_pk 
BEFORE INSERT ON pokemones_tipos 
FOR EACH ROW

BEGIN
  SELECT pokemones_tipos_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/

-- down

ALTER TABLE pokemones_tipos
DROP CONSTRAINT constraint_name;