from pymongo import MongoClient
from pymongo.synchronous.collection import Collection


class MongoConnectionManager:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection=None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        # self.connection = MongoClient('mongodb://127.0.0.1:27017/')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
# with MongoConnectionManager('127.0.0.1', 27017) as mongo:
#     db = mongo.admin
#     db.employee.insert_one({'name': 'Anand', 'age': 20})
#     db.employee.insert_one({'name': 'Suresh', 'age': 30})
#     db.employee.insert_one({'name': 'mahesh', 'age': 850})
#     db.employee.insert_one({'name': 'Ramesh', 'age': 40})
