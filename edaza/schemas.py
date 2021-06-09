from pydantic import BaseModel
from typing import List, Optional

class Food(BaseModel):

    name: str
    picture: str
    type: str
    category: str
    mode_of_preparation: str

    class Config:
        orm_mode = True


class Drink(BaseModel):

    title: str
    prep: str
    cook: str
    total_time: str
    yields: str
    no_of_recipe: str
    tags: str
    indgridients: str
    level: str
    rating: str
    drink_time: str
    drink_type: str
    description: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True

