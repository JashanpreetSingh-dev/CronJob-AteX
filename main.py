import pymongo

MONGO_CONNECTION_URI = 'mongodb+srv://JashanpreetSingh-dev:Jashan04$@cluster0.urbakzt.mongodb.net/?retryWrites=true&w=majority'


def write_data():
    Db_Client = pymongo.MongoClient(MONGO_CONNECTION_URI)
    db = Db_Client.get_database('prototype')
    collection = db.get_collection('orders')
    diction = {"name": "SomeOne'sName", "age": "NotTooOld"}
    # list_of_docs = get_all_products()['data']['orders']["edges"]
    collection.insert_one(diction)
