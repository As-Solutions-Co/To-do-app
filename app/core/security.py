from bcrypt import gensalt, hashpw, checkpw
from sqlmodel import Session, select
from uuid import UUID
from app.models import Token, User
from app.core.config import ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta, datetime, timezone
from typing import Any
from jwt import encode


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return checkpw(plain_password.encode(), hashed_password.encode())


def get_password_hash(password: str) -> str:
    bytes = password.encode()
    salt = gensalt()
    hashed_password = hashpw(bytes, salt).decode()
    return hashed_password


def get_user_by_email(*, session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    user_session = session.exec(statement).first()
    return user_session


def authenticate_user(*, session: Session, email: str, password: str) -> UUID | None:
    db_user = get_user_by_email(session=session, email=email)
    if not db_user:
        return None
    if not verify_password(password, db_user.password):
        return None
    return db_user


def generate_token(*, payload: str | Any) -> Token:
    expire_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + expire_delta
    to_encode = {"exp": expire, "data": str(payload)}
    return Token(access_token=encode(to_encode, SECRET_KEY, ALGORITHM))
