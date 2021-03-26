from fastapi import APIRouter

from src.api.api_v1.endpoints.user import router as user_router

api_routers = APIRouter()
api_routers.include_router(user_router, tags=["Users"])