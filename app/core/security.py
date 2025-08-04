from bcrypt import gensalt, hashpw, checkpw


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return checkpw(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    bytes = password.encode()
    salt = gensalt()
    hashed_password = hashpw(bytes, salt).decode()
    return hashed_password
