from fastapi import APIRouter, Depends
from app.api.deps import SessionDep, oauth2_scheme
from typing import Annotated
from app.models import UserRegister, User
from sqlmodel import select
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from app.core.security import get_password_hash, verify_password
from sqlalchemy.exc import IntegrityError


users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/register")
async def register(session: SessionDep, user: UserRegister):
    try:
        hashed_password = get_password_hash(user.password)
        new_user = User(
            email=user.email, fullname=user.fullname, password=hashed_password
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except IntegrityError:
        session.rollback()
        raise HTTPException(HTTP_400_BAD_REQUEST, "Email already exists")
