#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from turtle import st
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'USERDB' #enter your username
PASSWORD = 'PASSWORD' #enter your password
HOST = 'localhost' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
#SERVICE = 'your_oracle_service_name' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT)# + '/?service_name=' + SERVICE
engine = create_engine(ENGINE_PATH_WIN_AUTH)
session_db = sessionmaker()
session_db.configure(bind=engine)


def read():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM tipos WHERE id > 0
  """).format()
  return [dict(r) for r in conn.execute(stmt)]

def insert():
	conn = engine.connect()
	tipo = 'ULIMA 2'
	stmt = ("""
	  INSERT INTO tipos (nombre) 
	    VALUES ('{}')
	""").format(tipo)
	conn.execute(stmt)

def inserts_pokemones():
	archivo = open('data/pokemones.txt', 'r')
	lineas = archivo.readlines()
	resp = ''
	for linea in lineas:
		linea = linea.strip().split(',')
		numero = linea[0]
		nombre = linea[1]
		peso = linea[4]
		talla = linea[5]
		imagen = linea[6]
    genaracion_id = 0
    if numero >= 1 and numero <= 151:
      genaracion_id = 1
    elif numero >= 152 and numero <= 251:
      genaracion_id = 2
    elif numero >= 252 and numero <= 386:
      genaracion_id = 3
    elif numero >= 387 and numero <= 493:
      genaracion_id = 4
    elif numero >= 494 and numero <= 649:
      genaracion_id = 5
    elif numero >= 650 and numero <= 721:
      genaracion_id = 6
    else:
      generacion_id = 7
		stmt = ("INSERT INTO pokemones (nombre,numero,peso,talla,imagen,generacion_id) VALUES ('{}',{},{},{},'{}',{});\n").format(nombre, numero, peso, talla, imagen,genaracion_id)
		resp = resp + stmt
	
	with open('tmp/pokemones.txt', 'w') as f:
		f.write(resp.strip())

def llenar_tipos_pokemones():
  archivo = open('data/pokemones.txt', 'r')
  lineas = archivo.readlines()
  # tipos de la db
  tipos = {}
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM tipos
  """).format()
  rs = [dict(r) for r in conn.execute(stmt)]
  for r in rs:
    key = r['nombre']
    value = r['id']
    tipos[key] = value
  print(rs)
  # llenar asociativa
  for linea in lineas:
    linea = linea.strip().split(',')
    numero = linea[0]
    tipo1_id = tipos[linea[2]]
    tipo2_id = tipos[linea[3]]
    # concoer el id del pokemon con su numero
    stmt = ("""
      SELECT id FROM pokemones WHERE numero={};
    """).format(numero)
    pokemon = conn.execute(stmt).fetchone()
    pokemon_id = pokemon[0]
    # insertar en la asociativa
    stmt = ("""
      INSERT INTO pokemones_tipos (pokemon_id,tipo_id) 
        VALUES ({},{}),({},{});
    """).format(pokemon_id, tipo1_id,pokemon_id, tipo2_id,)
    conn.execute(stmt)

llenar_tipos_pokemones()