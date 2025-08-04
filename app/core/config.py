from os import getenv
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
DB_URL = getenv("DB_URL")
API_VERSION = getenv("API_VERSION")
