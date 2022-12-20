import os

from dotenv import load_dotenv

load_dotenv()

# MongoDB Config
MONGODB_ATLAS_URI = os.environ.get("MONGODB_ATLAS_URI")
