from fastapi import APIRouter
from app.api.routes import projects, tasks, users, login

api_router = APIRouter()
