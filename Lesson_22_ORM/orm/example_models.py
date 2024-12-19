
"""Db orm models."""
# https://docs.sqlalchemy.org/en/20/core/types.html
from sqlalchemy import Column, ForeignKey, Integer, String

from db_orm import Base


class Users(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)


class Orders(Base):

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product = Column(String(100), nullable=False)
    amount = Column(Integer)
