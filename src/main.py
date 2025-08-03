from src.tasks import tasks_router
from src.projects import projects_router
from src.auth import oauth2_scheme, auth_router
from fastapi import FastAPI, Depends
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()


app.include_router(auth_router)
app.include_router(tasks_router, dependencies=[Depends(oauth2_scheme)])
app.include_router(projects_router, dependencies=[Depends(oauth2_scheme)])
