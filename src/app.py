from fastapi import FastAPI
from src.db.base import Base


app: FastAPI = FastAPI()
db = Base.metadata