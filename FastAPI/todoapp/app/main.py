"""SQLALCHEMY tutorial on how to build an app"""

from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy.orm import session

import app.models as models
from app.models import Todos
from app.database import engine, sessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


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


@app.post("/")
async def read_all(db: db_annotation):
    """reading all from sqlite3 db"""
    return db.query(Todos).all()
