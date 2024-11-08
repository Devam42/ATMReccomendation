from database.mongo_connection import get_mongo_client
from database.data_inserter import insert_data
from data_generation.mentor_generator import generate_mentor_data
from data_generation.final_rating_generator import generate_final_rating_data
from config.settings import DATABASE_NAME

def main():
    # Connect to MongoDB
    client = get_mongo_client()
    if client is None:
        print("Failed to connect to MongoDB. Exiting.")
        return

    db = client[DATABASE_NAME]

    # Generate data
    num_entries = 5000
    correct_ratio = 2

    print("Generating mentor data...")
    mentor_data = generate_mentor_data(num_entries, correct_ratio)

    print("Generating final rating data...")
    final_rating_data = generate_final_rating_data(num_entries, correct_ratio)

    # Insert data into MongoDB
    recommendations_collection = db['RecommendationSystemDatabase']
    final_ratings_collection = db['FinalRating']

    insert_data(recommendations_collection, mentor_data)
    insert_data(final_ratings_collection, final_rating_data)

if __name__ == "__main__":
    main()
