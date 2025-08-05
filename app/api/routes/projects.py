from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.deps import oauth2_scheme

projects_router = APIRouter(prefix="/projects", tags=["projects"])


@projects_router.get("/test")
def test(token: Annotated[str, Depends(oauth2_scheme)]):
    return "hola"
