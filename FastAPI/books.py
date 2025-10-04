"""Our server launching here"""

from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Classic"},
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Classic",
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "category": "Programming",
    },
    {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programming"},
    {
        "title": "Sakouhi Legacy",
        "author": "Aymen",
        "category": "Biography",
    },
]


@app.get("/books")
async def read_all_books():
    """Get all books"""
    return BOOKS


@app.get("/books/{book_title}")
async def get_book_by_title(book_title: str):
    "Get a single book based on a dynamic title"
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def get_category_by_query(category: str):
    """Getting a book by searching its category"""
    books_to_return = []
    for book in BOOKS:
        if category.casefold() == book.get("category").casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_by_query(book_author: str, category: str):
    """return a book based on author name and category"""
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(
    new_book=Body(),
):
    """Adding a new book"""
    BOOKS.append(new_book)
