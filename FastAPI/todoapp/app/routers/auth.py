"""Everything protected here"""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session


from app.models import Users
from app.database import sessionLocal


router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


db_dependency = Annotated[Session, Depends(get_db)]


def authenticate_user(username: str, password: str, db: db_dependency):
    """check if user is correct or not"""
    user = db.query(Users).filter(username == Users.username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True


class CreateUserRequest(BaseModel):
    """a base model for the user creation query"""

    email: str = Field(min_length=6, email=True)
    username: str = Field(min_length=4, max_length=16)
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    password: str = Field(min_length=8)
    role: str = Field(min_length=4)

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "johndoe@gmail.com",
                "username": "johndoe",
                "first_name": "John",
                "last_name": "Doe",
                "password": "helloitsjohndoe",
                "role": "admin",
            }
        }
    }


@router.post("/auth/")
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    """User auth route example"""

    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
    )

    db.add(create_user_model)
    db.commit()

    return create_user_model


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    """Login for access token and get your token"""
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"
    return "Successful Authentication"
