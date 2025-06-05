from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)  # in centimeters
    weight = Column(Float)  # in kilograms

    fitness_records = relationship("FitnessRecord", back_populates="user")


class FitnessRecord(Base):
    __tablename__ = "fitness_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(String, nullable=False)  # YYYY-MM-DD format
    steps = Column(Integer)
    calories_burned = Column(Float)
    workout_minutes = Column(Float)

    user = relationship("User", back_populates="fitness_records")
