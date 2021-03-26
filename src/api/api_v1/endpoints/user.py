from typing import Any, List
import json

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from starlette.responses import Response
from src.api.utils.common import get_db

from src.models import User
from src import schemas
from src.core.return_messages import codes, ptBr
from src.api.message import Message
# from src.core.config import settings

router = APIRouter()

@router.get(
    '/get_user/{token}'
)
async def retrieve_user(
        token,
        db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.Token == str(token)).first()
    if not user:
        return Response(json.dumps({
                    "messageCode": codes['db'],
                    "message": ptBr['eUserNotFound']
                }),
                    status_code=404)
    
    return user


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