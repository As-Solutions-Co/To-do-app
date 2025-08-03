from fastapi import APIRouter


projects_router = APIRouter(prefix="/projects", tags=["projects"])


@projects_router.get("/get_projects")
def get_projects():
    pass
