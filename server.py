from bottle import Bottle, run
from main import engine
import json

app = Bottle()

@app.route('/', method='GET')
def home():
  return 'hola mundo'

@app.route('/listar', method='GET')
def listar():
  conn = engine.connect()
  stmt = ("""
    SELECT * FROM tipos WHERE id > 0
  """).format()
  return json.dumps([dict(r) for r in conn.execute(stmt)])

if __name__ == '__main__':
  run(
    app, 
    host='0.0.0.0', 
    port=8081, 
    debug=True, 
    reloader=True
  )