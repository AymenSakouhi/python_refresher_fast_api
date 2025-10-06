"""SQLALCHEMY tutorial on how to build an app"""

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import session
from starlette import status

from app.routers import auth
import app.models as models
from app.models import Todos
from app.database import engine, sessionLocal


router = APIRouter()

models.Base.metadata.create_all(bind=engine)

router.include_router(auth.router)


def get_db():
    """
    Dependency that provides a SQLAlchemy database session.

    Yields:
        db (Session): SQLAlchemy database session.
    Closes the session after the request is finished.
    """
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


# Define a reusable type annotation for the database session dependency.
# This uses Python's `Annotated` to combine the type (session) with the FastAPI dependency injection (`Depends(get_db)`).
db_annotation = Annotated[session, Depends(get_db)]


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_annotation):
    """reading all from sqlite3 db"""
    return db.query(Todos).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo_by_id(db: db_annotation, todo_id: int = Path(gt=0)):
    """getting a single to do by id"""
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code=404, detail="No todo found")


class TodoRequest(BaseModel):
    """Creating a class for the todos post request"""

    title: str = Field(min_length=1, max_length=60)
    description: str = Field(min_length=1, max_length=256)
    priority: int = Field(gt=0)
    complete: bool = Field(default=False)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Walk the dog",
                "description": "Just walk the dog whenver free today",
                "priority": 5,
                "complete": False,
            }
        }
    }


@router.post("/todo/create", status_code=status.HTTP_201_CREATED)
async def todo_create(db: db_annotation, todo_request: TodoRequest):
    """adding a todo"""
    new_todo = Todos(**todo_request.model_dump())
    db.add(new_todo)
    db.commit()


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def todo_update(
    todo_request: TodoRequest, db: db_annotation, todo_id: int = Path(gt=0)
):
    """updating a todo to DB with using both query and path id"""
    todo_model = db.query(Todos).filter(todo_id == Todos.id).first()
    if not todo_model:
        raise HTTPException(status_code=404, detail="No todo found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def todo_delete(db: db_annotation, todo_id: int = Path(gt=0)):
    """Adding a todo to DB with using both query and path id"""
    todo_model = db.query(Todos).filter(todo_id == Todos.id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="No todo found")

    db.query(Todos).filter(todo_id == Todos.id).delete()
    db.commit()
