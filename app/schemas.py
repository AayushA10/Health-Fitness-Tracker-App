from pydantic import BaseModel
from typing import List

class FitnessRecordBase(BaseModel):
    date: str
    steps: int
    calories_burned: float
    workout_minutes: float

class FitnessRecordCreate(FitnessRecordBase):
    pass

class FitnessRecord(FitnessRecordBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    age: int
    height: float
    weight: float

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    fitness_records: List[FitnessRecord] = []

    class Config:
        orm_mode = True
