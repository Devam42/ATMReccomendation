import json
import uuid
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# MongoDB connection details
username = 'kjxsofttechpvtltd'
password = quote_plus('Rz@Fas092311')  # URL-encode your password

# Construct the MongoDB URI
uri = f"mongodb+srv://{username}:{password}@kjxwebsite.3mup0.mongodb.net/?retryWrites=true&w=majority&appName=kjxwebsite"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")

# Select the database
db = client['Reccomendation']  # Use the 'Reccomendation' database

# Read data from RecommendationSystemDatabase.json
with open("RecommendationSystemDatabase.json", "r") as f:
    recommendation_data = json.load(f)

# Read data from FinalRating.json
with open("FinalRating.json", "r") as f:
    final_rating_data = json.load(f)

# Replace _id fields with UUIDs in recommendation data
for mentor in recommendation_data:
    mentor['_id'] = str(uuid.uuid4())

# Replace _id fields with UUIDs in final rating data
for entry in final_rating_data:
    entry['_id'] = str(uuid.uuid4())
    for mentee in entry.get('mentees', []):
        mentee['_id'] = str(uuid.uuid4())

# Insert data into MongoDB collections
recommendations_collection = db['RecommendationSystemDatabase']
final_ratings_collection = db['FinalRating']

# Insert recommendation data
try:
    recommendations_collection.insert_many(recommendation_data)
    print("Recommendation data inserted successfully into 'RecommendationSystemDatabase' collection.")
except Exception as e:
    print(f"An error occurred while inserting recommendation data: {e}")

# Insert final rating data
try:
    final_ratings_collection.insert_many(final_rating_data)
    print("Final rating data inserted successfully into 'FinalRating' collection.")
except Exception as e:
    print(f"An error occurred while inserting final rating data: {e}")
