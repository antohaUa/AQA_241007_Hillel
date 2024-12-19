"""Db orm models."""
# https://docs.sqlalchemy.org/en/20/core/types.html
from sqlalchemy import Column, ForeignKey, Integer, String

from db_orm import Base


class FitnessCenter(Base):
    """Table fitness_center."""

    __tablename__ = 'fitness_center'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    address = Column(String(50), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    contacts = Column(String(20), nullable=False)


class Rating(Base):
    """Table rating."""

    __tablename__ = 'rating'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    trainer = Column(Integer, ForeignKey('trainer.id'), nullable=False)
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    points = Column(Integer, default=0, nullable=False)
    text = Column(String(100), nullable=False)


class Reservation(Base):
    """Table reservation."""

    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    trainer = Column(Integer, ForeignKey('trainer.id'), nullable=False)
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    service = Column(Integer, ForeignKey('service.id'), nullable=False)
    date = Column(String(10), nullable=False)
    time = Column(String(10), nullable=False)


class Service(Base):
    """Table service."""

    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    duration = Column(Integer, default=0, nullable=False)
    description = Column(String(50), nullable=False)
    price = Column(Integer, default=0, nullable=False)
    fitness_center = Column(Integer, ForeignKey('fitness_center.id'), nullable=False)
    max_attendees = Column(Integer, default=1, nullable=False)


class ServicesBalance(Base):
    """Table service_balance."""

    __tablename__ = 'services_balance'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    service = Column(Integer, ForeignKey('service.id'), nullable=False)
    amount = Column(Integer, default=0, nullable=False)


class Trainer(Base):
    """Table trainer."""

    __tablename__ = 'trainer'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    fitness_center = Column(Integer, ForeignKey('fitness_center.id'), nullable=False)
    age = Column(Integer, default=18, nullable=False)
    sex = Column(String(6), nullable=False)


class TrainerCapacity(Base):
    """Table trainer_capacity."""

    __tablename__ = 'trainer_capacity'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    service = Column(Integer, ForeignKey('service.id'), nullable=False)
    trainer = Column(Integer, ForeignKey('trainer.id'), nullable=False)
    max_attendees = Column(Integer, default=1, nullable=False)


class TrainerSchedule(Base):
    """Table trainer_schedule."""

    __tablename__ = 'trainer_schedule'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    trainer = Column(Integer, ForeignKey('trainer.id'), nullable=False)
    date = Column(String(50), nullable=False)
    start_time = Column(String(50), nullable=False)
    end_time = Column(String(50), nullable=False)


class User(Base):
    """Table user."""

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    birth_date = Column(String(50), default='2000-01-01', nullable=False)
    phone = Column(String(50), nullable=False)
    funds = Column(Integer, default=0, nullable=False)
    email = Column(String(100), nullable=False)


class Test(Base):
    """Table user."""

    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    test = Column(String(50), nullable=False)
