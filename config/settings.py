import os
from urllib.parse import quote_plus

# Load environment variables
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

# MongoDB connection details
USERNAME = os.getenv('MONGODB_USERNAME')
PASSWORD = quote_plus(os.getenv('MONGODB_PASSWORD'))  # URL-encode the password
URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@kjxwebsite.3mup0.mongodb.net/?retryWrites=true&w=majority&appName=kjxwebsite"

# Database name
DATABASE_NAME = 'Reccomendation'
