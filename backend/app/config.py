import os
from dotenv import load_dotenv

load_dotenv()

# Simple configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "virtues_db")

print(MONGODB_URL)
print(DATABASE_NAME)
