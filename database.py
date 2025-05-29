from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///bookstore.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def init_db():
    from models import Category, Book  
    Base.metadata.create_all(engine)
