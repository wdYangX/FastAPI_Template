from sqlalchemy import Column, Integer, String, ForeignKey
from src.db.base_class import Base


class UserBase(Base):
    ID = Column(Integer, primary_key=True, index=True)
    Username = Column(String, nullable=False)
    Password = Column(String, nullable=False)
    Token = Column(String, nullable=False)
    First_Name = Column(String, nullable=True)
    Last_Name = Column(String, nullable=True)
    Phone = Column(String, nullable=True)
    Email = Column(String, unique=True, nullable=False)
    Country_ID = Column(Integer, ForeignKey("Country.ID"))


class User(Base):
    ID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(1000), unique=True, nullable=False)
    Password = Column(String(1000), nullable=False)
    Token = Column(String(255), nullable=False)
    First_Name = Column(String(100), nullable=True)
    Last_Name = Column(String(100), nullable=True)
    Phone = Column(String(50), nullable=True)
    Email = Column(String(255), unique=True, nullable=False)
    Country_ID = Column(String(255))
