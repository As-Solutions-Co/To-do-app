from fastapi import APIRouter, Depends
from app.api.deps import SessionDep
from typing import Annotated
from app.models import UserRegister, User
from sqlmodel import select
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from app.core.security import get_password_hash, verify_password


login_router = APIRouter(prefix="/login", tags=["login"])


@login_router.post("/register")
def register(session: SessionDep, user: UserRegister):
    existing_user = session.exec(select(User).where(User.email == user.email)).first()

    if existing_user:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Email already exists")

    hashed_password = get_password_hash(user.password)

    new_user = User(email=user.email, fullname=user.fullname, password=hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
