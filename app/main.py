from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from app.api.main import api_router
from app.core.config import API_VERSION
from app.core.db import create_db_and_tables
import time


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=f"/api/{API_VERSION}")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
