from passlib.context import CryptContext

ALGORITHM ='HS256'
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_token(plain_token: str, hashed_token: str):
    return pwd_context.verify(plain_token, hashed_token)


def get_token_hash(password: str):
    return pwd_context.hash(password)