from fastapi import APIRouter, Depends
from app.api.deps import SessionDep, oauth2_scheme
from typing import Annotated
from app.models import Token, UserRegister, User
from sqlmodel import select
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from app.core.security import generate_token, get_password_hash, verify_password
from sqlalchemy.exc import IntegrityError
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import authenticate_user


login_router = APIRouter(prefix="/login", tags=["login"])


@login_router.post("/access-token")
def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    email = form_data.username
    password = form_data.password
    user_id = authenticate_user(session=session, email=email, password=password)
    if not user_id:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Incorrect user or password")
    payload = {"user_id": user_id}
    return generate_token(payload=payload)
