from flask import Flask
from pymongo import MongoClient
import certifi
import configparser
import json

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://admin:admin1234@cluster1.odntcuv.mongodb.net/",
    tls=True,
    tlsCAFile=certifi.where()
)

db = client.configfile
col = db.configdata

#config parser object
config = configparser.ConfigParser()

try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Error reading config file: {e}")
    exit()


db_host = config['DATABASE']['host']
db_port = config['DATABASE']['port']
db_username = config['DATABASE']['username']
db_password = config['DATABASE']['password']

server_address = config['Server']['address']
server_port = config['Server']['port']


#Store the values in dictionary

configdata = {
                "database" : 
                {
                "host":db_host,
                "port":db_port,
                "username":db_username,
                "password":db_password
                },

                "server" : 
                {
                "address": server_address,
                "port":server_port
                }
            }

configdata_json = json.dumps(configdata)
print(type(configdata))
print(configdata_json)
print(type(configdata_json))

@app.route("/adddate",methods = ['POST'])
def adddata():
    db.configdata.insert_one(configdata)

    return "Output added successfully in database"

@app.route("/fetch", methods = ['GET'])
def fetch():
    data = []
    c = col.find({},{"_id":0})
    for i in c:
        data.append(i)
    return data

if __name__ == '__main__':
    app.run(debug=True)





