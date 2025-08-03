from fastapi import APIRouter


tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/get_tasks")
def get_tasks():
    pass


@tasks_router.post("/create_task")
def create_task():
    pass


@tasks_router.put("/update_task")
def update_task():
    pass


@tasks_router.delete("/delete_task")
def delete_task():
    pass
