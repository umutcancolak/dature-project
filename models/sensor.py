from db import mongo_db
import datetime

class Sensor(object):
    def __init__(self, _id, moisture, temperature, date=datetime.datetime.now()):
        self._id = _id
        self.date = date
        self.moisture = moisture
        self.temperature = temperature       
                
    def get_all(self):
        return [result for result in mongo_db.find("sensor_trial",{})]

    def save_to_mongo(self):
        mongo_db.insert("sensor_trial",self.json())

    def json(self):
        return {
            "id": self._id,
            "date": self.date,
            "temperature": self.temperature,
            "moisture" : self.moisture
        }