import jwt
import json
import src.crud.user as crud_user

from jwt import PyJWTError
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import Response
from sqlalchemy.orm import Session

from src.api.utils.common import get_db
from src.core import config
from src.core.security import ALGORITHM


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")

def get_environment_from_token(
    db: Session = Depends(get_db),
    token: str = Security(reusable_oauth2)
    ):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Token expirou/invalido"
        )
    return payload.get("environment")