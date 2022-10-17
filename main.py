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
  for r in conn.execute(stmt):
  	print(r)
  # print(rs)

def insert():
	conn = engine.connect()
	tipo = 'ULIMA 2'
	stmt = ("""
	  INSERT INTO tipos (nombre) 
	    VALUES ('{}')
	""").format(tipo)
	conn.execute(stmt)

read()
