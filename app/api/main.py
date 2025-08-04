from fastapi import APIRouter
from app.api.routes import projects, tasks, users, login

api_router = APIRouter()
api_router.include_router(login.login_router)
