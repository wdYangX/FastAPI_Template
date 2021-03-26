from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Country(Base):
    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Available = Column(Boolean, nullable=False, default=0)