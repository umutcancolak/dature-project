from flask_restful import Resource, reqparse 
from models.sensor import Sensor
from db import mongo_db

parser = reqparse.RequestParser()
parser.add_argument("sensor_id",
    type = int,
    required = True,
    help = "This field can not be left blank"
)
parser.add_argument("moisture",
    type = int,
    required = True,
    help = "This field can not be left blank"
)
parser.add_argument("temperature",
    type =int,
    required = True,
    help = "This field can not be left blank"
)

class SensorRegister(Resource):

    def get(self):
        mongo_db.find("sensor_trial",{})
        

        