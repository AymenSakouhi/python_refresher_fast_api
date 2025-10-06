"""Everything protected here"""

from datetime import timedelta, datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from jose import JWTError, jwt


from app.models import Users
from app.database import sessionLocal


router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "c3f7aca8f9f5ca94f18a7169ccfe44c935fdbc6e07c10d9380c54f26445cf299"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


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
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    """do the jwt token here"""
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + expires_delta

    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    """
    verifying user based on JWT token
    this should be used for the protected routes
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: str = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user"
            )
        return {"username": username, "id": user_id}
    except JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user"
        ) from exc


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


class Token(BaseModel):
    """response model for our jwt token encoding"""

    access_token: str
    token_type: str


@router.post("/")
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


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    """Login for access token and get your token"""
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user"
        )
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}
