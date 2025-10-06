"""SQLALCHEMY tutorial on how to build an app"""

from fastapi import FastAPI

from app.routers import auth, todos
import app.models as models
from app.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
