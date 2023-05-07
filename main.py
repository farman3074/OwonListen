from flask import Flask,request,jsonify
#from db import update_db_lastping

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


@app.route('/',methods = ['POST','GET'])
def index():
  if request.method == 'POST':
    return 'we got a POST'
  else:
    return 'SOMETHING ELSE'
  #content = jsonify(request.json)
  #print(content)
  #result = update_db_lastping(content)
  #return content

if __name__ == "__main__" :
  app.run(host="0.0.0.0", debug=True)

#app.run(host='0.0.0.0', port=8080)
