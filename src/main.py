from fastapi import FastAPI
from .tasks import tasks_router
from .projects import projects_router

app = FastAPI()


app.include_router(tasks_router)
app.include_router(projects_router)
