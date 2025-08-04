from app.core.db import engine
from sqlmodel import Session
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.core.config import API_VERSION


def get_session():
    with Session(engine) as session:
        yield session


oauth2_scheme = OAuth2PasswordBearer("token")
SessionDep = Annotated[Session, Depends(get_session)]
