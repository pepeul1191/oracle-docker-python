# Docker - Oracle Express XE 11g

## Python Client

Instalar y activar el ambiente virtual - Linux:

    $ sudo apt install python3-virtualenv python3-venv
    $ python3 -m venv ./env
    $ source env/bin/activate

Instalar y activar el ambiente virtual - Windows:

    > pip install virtualenv
    > virtualenv env
    > env\Scripts\activate.bat

Arrancar aplicación:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ mkdir static/uploads
    $ python main.py

## Agregar librerías de python - oracle

Instalar liberías:

	$ sudo apt-get install build-essential unzip python-dev libaio-dev libaio1

Descargar desde http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html:

+ instantclient-basic-linux
+ instantclient-sdk-linux

Crear una carpeta en <b>/home/{user}<b> llamada oracle. Luego agregar las variables de entorno:

		$ sudo pluma ~/.profile
		export ORACLE_HOME=/location/of/your/files/instantclient_11_2
		export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
		$ source ~/.profile

Editar /etc/ld.so.conf.d/oracle.conf

		sudo ldconfig


## Docker

Ver lista de containers deplegados

	$ docker ps

Arrancar containers en base a lo escrito en .yml

	$ docker compose up

Acceder al bash del container:

	$ docker exec -it <id_container> bash
	# sqlplus
	user: system - password: oracle	

Creación de usuario:

	CREATE TABLESPACE TSD_USERDB LOGGING DATAFILE 'TSD_USERDB.DBF' SIZE 200M AUTOEXTEND ON NEXT 200M MAXSIZE 400M;
	CREATE TABLESPACE TSI_USERDB LOGGING DATAFILE 'TSI_USERDB.DBF' SIZE 200M AUTOEXTEND ON NEXT 50M MAXSIZE 400M;
	CREATE USER USERDB IDENTIFIED BY PASSWORD DEFAULT TABLESPACE TSI_USERDB QUOTA UNLIMITED ON TSD_USERDB QUOTA UNLIMITED ON TSI_USERDB;

Permisos a usuario:

	GRANT CREATE SESSION TO USERDB;
	GRANT CREATE PROCEDURE TO USERDB;
	GRANT CREATE VIEW TO USERDB;
	GRANT CREATE TABLE TO USERDB;
	GRANT CREATE SEQUENCE TO USERDB;
	GRANT CREATE TRIGGER TO USERDB;

Borrar containers:

	$ docker container rm -f <id_container>

---

Fuentes:

+ https://www.youtube.com/watch?v=E170aADKxh8
+ https://hub.docker.com/r/oracleinanutshell/oracle-xe-11g
+ https://gitea.com/docker_test/oracle
+ https://rmauro.dev/oracle-database-on-docker-for-development/
+ https://www.techonthenet.com/oracle/questions/insert_rows.php
+ https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
+ https://gist.github.com/kimus/10012910
