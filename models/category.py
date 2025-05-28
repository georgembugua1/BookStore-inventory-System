from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from database import Base, Session

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    books = relationship('Book', back_populates='category', cascade='all, delete-orphan')

    @validates('name')
    def validate_name(self, key, value):
        value = value.strip() if value else value
        if not value or len(value) < 3:
            raise ValueError('Category name must be at least 3 characters long.')
        return value

    @classmethod
    def create(cls, name):
        session = Session()
        try:
            name = name.strip()
            if session.query(cls).filter_by(name=name).first():
                raise ValueError(f"Category name '{name}' already exists.")
            category = cls(name=name)
            session.add(category)
            session.commit()
            return category
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, category_id):
        session = Session()
        try:
            category = session.get(cls, category_id)
            if not category:
                raise ValueError(f"Category with ID {category_id} not found.")
            session.delete(category)
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
    def find_by_id(cls, category_id):
        session = Session()
        try:
            return session.get(cls, category_id)
        finally:
            session.close()

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
