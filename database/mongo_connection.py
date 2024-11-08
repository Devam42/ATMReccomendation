from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config.settings import URI

def get_mongo_client():
    """
    Establish a connection to MongoDB and return the client object.
    """
    client = MongoClient(URI, server_api=ServerApi('1'))
    # Test the connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. Successfully connected to MongoDB!")
    except Exception as e:
        print(f"An error occurred: {e}")
        client = None
    return client
