
from mongodbconnectionmanager import MongoConnectionManager
with MongoConnectionManager('127.0.0.1', 27017) as mongo:
    print('Inserting single objects into Mongo Collection')
    db = mongo.admin#Get DB
    collection = db.employee
    rowupdated = db.employee.insert_one({'name': 'Geeta', 'age': 20})
    print(rowupdated)
    db.employee.insert_one({'name': 'Manya', 'age': 30})
    db.employee.insert_one({'name': 'Anu', 'age': 850})
    db.employee.insert_one({'name': 'Roopa', 'age': 40})

    print('Print All objects From Mongo Collection')
    cursor = collection.find()
    document_count = collection.count_documents({})
    print(document_count)
    cursor.batch_size(20)
    for document in cursor:
        employee_name=document.get('name')
        print(employee_name)
