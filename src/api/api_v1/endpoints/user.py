from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from src.api.utils.common import get_db

from src import models, schemas
# from src.core.config import settings

router = APIRouter()

@router.get(
    '/get_user/{token}'
)
async def retrieve_user(
        token
):
    # user = db.query(User).filter(User.id == str(user_id)).first()
    # if not user:
    #     return Response(json.dumps({
    #         "messageCode": codes['db'],
    #         "message": ptBr['eUserNotFound']
    #     }),
    #         status_code=404)
    
    return ''


@router.post(
    '/create_user',
    response_model=schemas.User
)
async def create_user(
        data: schemas.user.UserCreate,
        db: Session = Depends(get_db)
):
    new_user = data.user_data
    new_user.password = get_password_hash(new_user.password)
    user_validated = schemas.user.UserCreate(**new_user.dict())
    user = schemas.User(**user_validated.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user