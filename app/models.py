from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


# generic models
class StatusEnum(str, Enum):
    over_due = "Over due"
    on_time = "On time"
    in_progress = "In progress"
    pending = "Pending"
    done = "Done"
    canceled = "Canceled"


# User entity


class UserRegister(SQLModel):
    fullname: str = Field(min_length=5, max_length=200)
    email: EmailStr = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)


class User(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    fullname: str = Field(min_length=5, max_length=200)
    email: EmailStr = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)

    projects: List["Project"] = Relationship(back_populates="owner")


# Project entity
class Project(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: str = Field(nullable=False)
    description: str
    due_datetime: datetime
    status: StatusEnum = Field(default=StatusEnum.pending, nullable=False)

    owner_id: UUID = Field(foreign_key="user.id", index=True, nullable=False)
    owner: "User" = Relationship(back_populates="projects")

    tasks: List["Task"] = Relationship(back_populates="project")


class Task(SQLModel, table=True):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    name: str = Field(max_length=50, nullable=False)
    description: str = Field(nullable=False)
    due_datetime: datetime = Field(nullable=False)
    status: StatusEnum = Field(default=StatusEnum.pending, nullable=False)

    project_id: UUID = Field(foreign_key="project.id", nullable=False)
    project: "Project" = Relationship(back_populates="tasks")


# Token model


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
