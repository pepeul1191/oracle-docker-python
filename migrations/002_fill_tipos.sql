-- up
INSERT ALL
    INTO tipos(nombre) VALUES ('PLANTA')
    INTO tipos(nombre) VALUES ('VENENO')
    INTO tipos(nombre) VALUES ('FUEGO')
    INTO tipos(nombre) VALUES ('NINGUNO')
    INTO tipos(nombre) VALUES ('VOLADOR')
    INTO tipos(nombre) VALUES ('AGUA')
    INTO tipos(nombre) VALUES ('BICHO')
    INTO tipos(nombre) VALUES ('NORMAL')
    INTO tipos(nombre) VALUES ('ELÉCTRICO')
    INTO tipos(nombre) VALUES ('TIERRA')
    INTO tipos(nombre) VALUES ('HADA')
    INTO tipos(nombre) VALUES ('LUCHA')
    INTO tipos(nombre) VALUES ('PSÍQUICO')
    INTO tipos(nombre) VALUES ('ROCA')
    INTO tipos(nombre) VALUES ('ACERO')
    INTO tipos(nombre) VALUES ('HIELO')
    INTO tipos(nombre) VALUES ('FANTASMA')
    INTO tipos(nombre) VALUES ('DRAGÓN')
    INTO tipos(nombre) VALUES ('SINIESTRO')
SELECT * FROM dual;

-- down

TRUNCATE TABLE tipos;
ALTER SEQUENCE tipos LAST_NUMBER 1;