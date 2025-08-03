from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from .settings import pwd_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from pydantic import BaseModel

from fastapi import APIRouter


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
auth_router = APIRouter(prefix="/auth", tags=["auth"])


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


@auth_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return Token(
        access_token=f"username {form_data.username},password: {form_data.password}",
        token_type="bearer",
    )


@auth_router.get("/test")
async def test(token: Annotated[str, Depends(oauth2_scheme)]):
    hola = "hola"
    pass
