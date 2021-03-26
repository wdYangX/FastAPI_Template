from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class User(Base): 
    ID = Column(Integer, primary_key=True, index=True)
    Username = Column(String, nullable=False)
    Password = Column(String, nullable=False)
    Token = Column(String, nullable=False)
    First_Name = Column(String, nullable=True)
    Last_Name = Column(String, nullable=True)
    Phone = Column(String, nullable=True)
    Email = Column(String, unique=True, nullable=False)
    Country_ID = Column(Integer, ForeignKey("Country.ID"))

