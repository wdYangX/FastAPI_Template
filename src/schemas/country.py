from typing import Optional

from pydantic import BaseModel


# Shared properties
class CountryBase(BaseModel):
    ID: int
    Name: str
    Available: bool


# Properties to receive via API on creation
class CountryCreate(CountryBase):
    Name: str


# Properties to receive via API on update
class CountryUpdate(CountryBase):
    Password: Optional[str] = None


class CountryInDBBase(CountryBase):
    ID: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Country(CountryInDBBase):
    pass


# Additional properties stored in DB
class CountryInDB(CountryInDBBase):
    Name: str