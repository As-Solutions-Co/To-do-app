from sqlmodel import SQLModel, create_engine

from app.core.config import DB_URL


engine = create_engine(DB_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
