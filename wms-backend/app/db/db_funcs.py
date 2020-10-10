from sqlalchemy.orm import Session

from app.db.all import *
from .session import engine, SessionLocal

def create():
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    get_db func. db kullanacak fonksiyonlar için Depends yazmak amacıyla. her routes içinde import ediliyor.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
