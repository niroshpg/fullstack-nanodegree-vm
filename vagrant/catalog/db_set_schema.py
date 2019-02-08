import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    description = Column(String(250))
    author = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'description': self.description,
            'author': self.author,
            'id': self.id,
            'category_id': self.category_id,
        }


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    items = relationship(Item, backref="category",
                         passive_deletes=True, cascade="all")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'id': self.id,
            'items': [i.serialize for i in self.items]
        }


engine = create_engine('sqlite:///catalogue.db')
Base.metadata.create_all(engine)
