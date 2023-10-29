from app.models.models import user
from fastapi import APIRouter, Depends, Response
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.schemas.user import User_create
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.get("/user")
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    query = select(user)
    result = await session.execute(query)
    dict_user = dict()
    res = []
    for el in result.all():
        dict_user.update({"id": el[0]})
        dict_user.update({"name": el[1]})
        dict_user.update({"email": el[2]})
        dict_user.update({"user_id": el[3]})
        dict_user.update({"created_at": el[4]})
        res.append(el)
    return {"res": res}

@router.post("/user/new_user")
async def add_specific_users(new_user: User_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(user).values(**new_user.dict())
    await session.execute(stmt)
    await session.commit()
    print(new_user.dict().get("id"))
    query = select(user).where(user.c.id == new_user.dict().get("id"))
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"status": "good",
            "added_user": res
            }

@router.post("/user/user_id")
async def find_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(user).where(user.c.id == user_id)
    result = await session.execute(query)
    dict_user = dict()
    res = []
    for el in result.all():
        dict_user.update({"id": el[0]})
        dict_user.update({"name": el[1]})
        dict_user.update({"email": el[2]})
        dict_user.update({"user_id": el[3]})
        dict_user.update({"created_at": el[4]})
        res.append(el)
    return {
            "dict_user": dict_user,
            "finded_user": res
    }

@router.post("/user/user_id")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(user).where(user.c.id == user_id)
    result = await session.execute(query)
    stmt = delete(user).where(user.c.id == user_id)
    await session.execute(stmt)
    await session.commit()
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}
