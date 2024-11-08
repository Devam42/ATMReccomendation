import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
from bson import ObjectId
from datetime import datetime

# Custom JSON encoder
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

# MongoDB connection details
username = 'kjxsofttechpvtltd'
password = quote_plus('Rz@Fas092311')  # Replace with your actual password

# Construct the MongoDB URI
uri = f"mongodb+srv://{username}:{password}@kjxwebsite.3mup0.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))

# Select the database and collection
db = client['Reccomendation']
collection = db['FinalRating']

# Retrieve all documents from the collection
documents = list(collection.find())

# Write to JSON file
with open('final_rating_data.json', 'w') as f:
    json.dump(documents, f, cls=JSONEncoder, indent=4)

print("Data has been successfully exported to 'final_rating_data.json'")
