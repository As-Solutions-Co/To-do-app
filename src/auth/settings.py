from os import getenv
from passlib.context import CryptContext


SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
