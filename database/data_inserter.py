# database/data_inserter.py
def insert_data(collection, data):
    """
    Inserts data into the specified MongoDB collection.
    """
    try:
        collection.insert_many(data)
        print(f"Data inserted successfully into '{collection.name}' collection.")
    except Exception as e:
        print(f"An error occurred while inserting data into '{collection.name}': {e}")
