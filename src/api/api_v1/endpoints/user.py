import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import Response
from src.api.utils.common import get_db
from src.core.security import get_token_hash, verify_token
from src.crud import CRUDBase
from src.crud.crud_user import CRUDUser

# from src.models import User
from src import models
from src.schemas import User, UserUpdate, UserCreate
from src.core.return_messages import codes, ptBr

# from src.core.config import settings

router = APIRouter()
instance_user = CRUDUser(models.User)


@router.get(
    '/get_user/{token}'
)
async def retrieve_user(
        token,
        db: Session = Depends(get_db),
):
    user = instance_user.get(db, token)
    if not user:
        return Response(json.dumps({
                    "messageCode": codes['db'],
                    "message": ptBr['eUserNotFound']
                }),
                    status_code=404)
    
    return user


@router.post(
    '/create_user',
    response_model=User
)
async def create_user(
        data: UserCreate,
        db: Session = Depends(get_db)
):
    """
       Create new user.
       """
    # TODO: Check user is alredy exist
    # Define function into util folder with check user
    user = None
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    new_user = data
    token = get_token_hash(new_user.Password)
    user_validated = UserCreate(**new_user.dict())
    user_model = models.user.User(**user_validated.dict())
    user_model.Token = token
    user = instance_user.create(db, obj_in=user_model)
    # TODO: Define function verify email user

    return user


@router.put(
    '/update_user',
    response_model=User
)
async def update_user(
        data: UserUpdate,
        db: Session = Depends(get_db)
):
    """
        Update own user.
        """
    new_user = data
    user = instance_user.get(db, username=new_user.Username)
    if verify_token(plain_token=user.Token, hashed_token=get_token_hash(new_user.Password)):
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )

    user = instance_user.update(db, db_obj=user, obj_in=new_user)
    return user

@router.get(
    '/users'
)
async def list_users(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
):
    users = instance_user.get_multi(db, skip=skip, limit=limit)
    if not users:
        return Response(json.dumps({
            "messageCode": codes['db'],
            "message": ptBr['eNotAnyUsers']
        }),
            status_code=404)

    return users