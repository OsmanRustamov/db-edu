from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Header, HTTPException
from backend.common.database import Database


async def get_session() -> Session | Exception:
    return Database.get_session()


async def get_token_header(x_token: Annotated[str, Header()] = None):
    if x_token is None:
        raise HTTPException(status_code=400, detail='Token not found')
    if x_token != '123456789':
        raise HTTPException(status_code=401, detail='Operation Forbidden')
