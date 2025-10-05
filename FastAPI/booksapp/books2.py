"""a web server with fastapi"""

from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status


app = FastAPI()


class BOOK:
    """Books class"""

    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        """
        Purpose: a class for initiating books
        """

        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

    # end of constructor


class BookRequest(BaseModel):
    """base modal pydantic object of the book request"""

    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=150)
    rating: int = Field(gt=0, lt=6)
    published_date: Optional[int] = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Aymen",
                "description": "hello world!",
                "rating": 5,
                "published_date": "2025-01-01",
            }
        }
    }


BOOKS = [
    BOOK(
        1,
        "1984",
        "George Orwell",
        "A dystopian novel set in Airstrip One.",
        5,
        2025,
    ),
    BOOK(
        2,
        "To Kill a Mockingbird",
        "Harper Lee",
        "A novel about racial injustice in the Deep South.",
        5,
        2026,
    ),
    BOOK(
        3,
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        "A story of the Jazz Age in 1920s America.",
        4,
        2021,
    ),
    BOOK(
        4,
        "The Pragmatic Programmer",
        "Andrew Hunt",
        "A guide to pragmatic software development.",
        5,
        2012,
    ),
    BOOK(
        5,
        "Clean Code",
        "Robert C. Martin",
        "A handbook of agile software craftsmanship.",
        5,
        2022,
    ),
    BOOK(
        6,
        "Sakouhi Legacy",
        "Aymen",
        "Biography of Aymen's journey.",
        2,
        2030,
    ),
    BOOK(
        7,
        "Sakouhi From Zero to Top",
        "Aymen",
        "Aymen's rise to success.",
        3,
        2014,
    ),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books():
    """getting all books"""
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    """find book by path parameter"""
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found in detail")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    """get book by query params of rating"""
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(publish_date: int = Query(gt=1999, lt=2031)):
    """get the books by query param publish date"""
    books_to_return = []
    for book in BOOKS:
        if book.published_date == publish_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book/", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    """Adding a new book to the list"""
    new_book = BOOK(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return {"message": "book added"}


def find_book_id(book: BOOK):
    """find correct id"""
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book/", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    """update a book by its id as a path param and a new book as a query"""
    book_changed = False
    for i, item in enumerate(BOOKS):
        if item.id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    """delete book a book by its id as a path"""
    book_deleted = False
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="not found")
