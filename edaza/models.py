from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from edaza.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")



class Food(Base):

    __tablename__ = "Food"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    picture = Column(String, index=True)
    type = Column(String, index=True)
    category = Column(String, index=True) 
    mode_of_preparation = Column(String, index=True)

class Recipe(Base):
    
    __tablename__ = "Recipe"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    temperature = Column(String, index=True)
    time = Column(String, index=True)
    tags = Column(String, index=True)
    indgridients = Column(String, index=True)
    level = Column(String, index=True)
    rating = Column(String, index=True)
    description = Column(String, index=True)

class Drinks(Base):
    __tablename__ = "Drinks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    temperature = Column(String, index=True)
    time = Column(String, index=True)
    indgridients = Column(String, index=True)
    level = Column(String, index=True)
    rating = Column(String, index=True)
