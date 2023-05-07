from flask import Flask,request,jsonify
from db import update_db
import json

# initialize Connector object
#connector = Connector()

# function to return the database connection object
#def getconn():
 #   conn = connector.connect(
  #      os.environ['DB_CONNECT_STR_DEV'],
  #      "pymysql",
  #      user="owon-raw-db",
  #      password="Industrial420!",
  #      db="owondevices"
  #  )
  #  return conn

# create connection pool with 'creator' argument to our connection object function
#engine = create_engine(
#    "mysql+pymysql://",
#    creator=getconn,
#)

#PRODUCTION
#db_connection_str = os.environ['DB_CONNECT_STR']
#DEVELOPMENT
#dfddgsdgdgs

app = Flask(__name__)


@app.route('/',methods = ['POST'])
def index():
  if request.method == 'POST':
  #  return 'we got a POST'
    content = request.get_json()
    sjson = content['sjson']
    argJson = json.loads(sjson)
    argument = argJson['argument']
   # current = str(argument['current'])
    #return argJson['command']
    #print(content)
    command = argJson['command']
    if command == "mainData":
      query = "insert into rawdata (command,code,mac,token,ts,demandformatting,sumformatting,sum,ep,ieee,demand,meterstatus,current,unit,divisor,reactivesum,multiplier,reactivedemand,powerfactor,type) values ('" + command + "','" + content['code'] + "','" + content['mac'] + "','" + content['token'] + "','" + content['ts'] + "'," + str(argument['demandFormatting']) +"," + str(argument['sumFormatting']) + "," + str(argument['sum']) + "," + str(argument['ep']) + ",'" + argument['ieee'] + "'," + str(argument['demand']) + "," + str(argument['meterStatus']) + "," + str(argument['current']) + "," + str(argument['unit']) + "," + str(argument['divisor']) + "," + str(argument['reactiveSum']) + "," + str(argument['multiplier']) + "," + str(argument['reactiveDemand']) + "," + str(argument['powerFactor']) + ",'" + argJson['type'] + "')"
    
    if command == "L1/AData":
     query = "insert into rawdata (command,code,mac,token,ts,sum,ep,ieee,demand,current,reactivesum,reactivedemand,powerfactor,voltage,type) values ('" + command + "','" + content['code'] + "','" + content['mac'] + "','" + content['token'] + "','" + content['ts'] + "'," + str(argument['sum']) + "," + str(argument['ep']) + ",'" + argument['ieee'] + "'," + str(argument['demand']) + "," + str(argument['current']) + ","  + str(argument['reactiveSum']) + "," + str(argument['reactiveDemand']) + "," + str(argument['powerFactor']) + "," + str(argument['voltage']) + ",'" + argJson['type'] + "')"  
    
    if command == "L2/BData":
     query = "insert into rawdata (command,code,mac,token,ts,sum,ep,ieee,demand,current,reactivesum,reactivedemand,powerfactor,voltage,type) values ('" + command + "','" + content['code'] + "','" + content['mac'] + "','" + content['token'] + "','" + content['ts'] + "'," + str(argument['sum']) + "," + str(argument['ep']) + ",'" + argument['ieee'] + "'," + str(argument['demand']) + "," + str(argument['current']) + ","  + str(argument['reactiveSum']) + "," + str(argument['reactiveDemand']) + "," + str(argument['powerFactor']) + "," + str(argument['voltage']) + ",'" + argJson['type'] + "')"
      
    if command == "L3/CData":
     query = "insert into rawdata (command,code,mac,token,ts,sum,ep,ieee,demand,current,reactivesum,reactivedemand,powerfactor,voltage,type) values ('" + command + "','" + content['code'] + "','" + content['mac'] + "','" + content['token'] + "','" + content['ts'] + "'," + str(argument['sum']) + "," + str(argument['ep']) + ",'" + argument['ieee'] + "'," + str(argument['demand']) + "," + str(argument['current']) + ","  + str(argument['reactiveSum']) + "," + str(argument['reactiveDemand']) + "," + str(argument['powerFactor']) + "," + str(argument['voltage']) + ",'" + argJson['type'] + "')"

    if command == "humi":
      query = "insert into rawdata (command,code,mac,token,ts,humi,ep,ieee,type) values ('" + command + "','" + content['code'] + "','" + content['mac'] + "','" + content['token'] + "','" + content['ts'] + "'," + str(argument['humi']) + "," + str(argument['ep']) + ",'" + argument['ieee'] + "','" + argJson['type'] + "')"  

    if command == "temp":
      query = "insert into rawdata (command,code,mac,token,ts,temp,ep,ieee,type) values ('" + command + "','" + content['code'] + "','" + content['mac'] + "','" + content['token'] + "','" + content['ts'] + "'," + str(argument['temp']) + "," + str(argument['ep']) + ",'" + argument['ieee'] + "','" + argJson['type'] + "')"
      
    result = update_db(query)
    return 'result'
  else:
    return 'SOMETHING ELSE'
  #content = jsonify(request.json)
  #print(content)
  #result = update_db_lastping(content)
  #return content

if __name__ == "__main__" :
  app.run(host="0.0.0.0", debug=True)
  #app.run(host='0.0.0.0', port=8080)
