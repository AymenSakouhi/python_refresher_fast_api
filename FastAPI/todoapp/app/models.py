"""setting up models"""

from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base


class Todos(Base):
    """Adding a todos database class or a model persay"""

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
