import datetime
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./deltahacks6-51680-firebase-adminsdk-prd82-104625e207.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


class Value:
    Moisture = 0
    Temprature = 0
    date_added = datetime.datetime.now()

    def __init__(self, Moisture, Temprature):
        self.Moisture = Moisture
        self.Temprature = Temprature
        self.date_added = datetime.datetime.now()


class DatabaseManager:

    def __init__(self, db_name):
        self.ref = db.collection(u'test')

    def add_to_db(self, data):
        new_data = self.ref.add({
            'Moisture': data.Moisture,
            'Temperature': data.Temprature,
            'Date_added': data.date_added
        })

        return new_data

# #DEBUG
# object1 = Value(33, 22)
# dbm = dataBaseManager("test")
# dbm.add_to_db(object1)

