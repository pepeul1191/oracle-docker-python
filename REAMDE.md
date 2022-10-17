# Docker - Oracle Express XE 11g

Ver lista de containers deplegados

	$ docker ps

Arrancar containers en base a lo escrito en .yml

	$ docker compose up

Acceder al bash del container:

	$ docker exec -it <id_container> bash
	# sqlplus
	user: system - password: oracle	

Borrar containers:

	$ docker container rm -f <id_container>

---

Fuentes:

+ https://www.youtube.com/watch?v=E170aADKxh8
+ https://hub.docker.com/r/oracleinanutshell/oracle-xe-11g
+ https://gitea.com/docker_test/oracle
