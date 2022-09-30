import pymongo
import requests

MONGO_CONNECTION_URI = 'mongodb+srv://JashanpreetSingh-dev:Jashan04$@cluster0.urbakzt.mongodb.net/?retryWrites=true&w=majority'
URL = "https://objectivismrelativism.myshopify.com"
ACCESS_TOKEN = "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"
SECRET_KEY = "b5bc98ad3199589679bd85781661a86f"
API_KEY = "e892c944852691aca4b235bf7ec67ae4"


def get_unicorns():
    response = requests.get('https://frozen-tor-00688.herokuapp.com/api/v1/unicorns')
    return response.json()


def write_data():
    Db_Client = pymongo.MongoClient(MONGO_CONNECTION_URI)
    db = Db_Client.get_database('prototype')
    collection = db.get_collection('orders')
    # diction = {"name": "SomeOne'sName", "age": "NotTooOld"}
    list_of_docs = get_unicorns()
    collection.insert_one(list_of_docs)
