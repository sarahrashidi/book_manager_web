from sqlalchemy.orm import Session
from models import Book

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, author: str, year: int):
    db_book = Book(title=title, author=author, year=year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def update_book(db: Session, book_id: int, title: str = None, author: str = None, year: int = None):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None
    if title:
        db_book.title = title
    if author:
        db_book.author = author
    if year:
        db_book.year = year
    db.commit()
    db.refresh(db_book)
    return db_book
