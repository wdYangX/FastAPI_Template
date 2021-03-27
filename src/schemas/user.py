from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    ID: int
    Username: str
    Password: str
    Token: str
    First_Name: str
    Last_Name: str
    Phone: str
    Email: EmailStr
    Country_ID: int


# Properties to receive via API on creation
class UserCreate(BaseModel):
    ID: Optional[int] = None
    Username: str
    Password: str


# Properties to receive via API on update
class UserUpdate(BaseModel):
    Username: str
    Password: Optional[str]
    First_Name: str
    Last_Name: str
    Phone: str
    Email: EmailStr
    Country_ID: int


class UserInDBBase(UserBase):
    ID: Optional[int] = None
    Username: str
    Password: str
    Token: str
    First_Name: Optional[str] = None
    Last_Name: Optional[str] = None
    Phone: Optional[str] = None
    Email: Optional[str] = None
    Country_ID: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    Password: str