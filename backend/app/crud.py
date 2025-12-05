from sqlalchemy.orm import Session
from . import models, schemas

def get_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        description=book.description,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

