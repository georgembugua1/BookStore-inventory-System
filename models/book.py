from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from database import Base, Session
from models.category import Category

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', back_populates='books')

    @validates('title')
    def validate_title(self, key, value):
        value = value.strip() if value else value
        if not value or len(value) < 2:
            raise ValueError('Book title must be at least 2 characters long.')
        return value

    @validates('quantity')
    def validate_quantity(self, key, value):
        if value is None or value < 0:
            raise ValueError('Book quantity must be non-negative.')
        return value

    @classmethod
    def create(cls, title, quantity, category_id):
        session = Session()
        try:
           
            if not session.get(Category, category_id):
                raise ValueError(f"Category with ID {category_id} does not exist.")
            book = cls(title=title, quantity=quantity, category_id=category_id)
            session.add(book)
            session.commit()
            return book
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, book_id):
        session = Session()
        try:
            book = session.get(cls, book_id)
            if not book:
                raise ValueError(f"Book with ID {book_id} not found.")
            session.delete(book)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, book_id):
        session = Session()
        try:
            return session.get(cls, book_id)
        finally:
            session.close()

    @classmethod
    def filter_by_category(cls, books, category_id):
       
        count = 0
        insert_pos = 0
        for i in range(len(books)):
            if books[i].category_id == category_id:
                if count < 2:
                    books[insert_pos] = books[i]
                    insert_pos += 1
                    count += 1
            else:
                books[insert_pos] = books[i]
                insert_pos += 1
        return books[:insert_pos], insert_pos

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', category_id={self.category_id}, quantity={self.quantity})>"
