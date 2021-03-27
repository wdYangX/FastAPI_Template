from typing import Optional, Any, Union, Dict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.core.security import get_token_hash
from src.models.user import User
from src.crud.base import CRUDBase
from src.schemas import UserUpdate


class CRUDUser(CRUDBase):
    def get(self, db: Session, username: Any) -> Optional[User]:
        return db.query(self.model).filter(User.Username == username).first()

    def update(
            self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        # TODO: Must be check Country_ID
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        setattr(db_obj, "Token", get_token_hash(update_data['Password']))

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj