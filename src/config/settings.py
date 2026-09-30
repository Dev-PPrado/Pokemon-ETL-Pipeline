from dotenv import load_dotenv
import os

load_dotenv()

POKEAPI_URL = os.getenv("POKEAPI_URL")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", 10))
DATABASE_URL = os.getenv("DATABASE_URL")