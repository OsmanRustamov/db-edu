from app.models.models import user
from fastapi import APIRouter, Depends, Response
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.schemas.user import User_create
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.get("/user")
async def get_all_users(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(user)
    result = await session.execute(query)
    dict_user = dict()
    res = []
    for el in result.all():
        dict_user.update({"id": el[0]})
        dict_user.update({"name": el[1]})
        dict_user.update({"email": el[2]})
        dict_user.update({"tariff_id": el[3]})
        dict_user.update({"created_at": el[4]})
        res.append(el)
    return {"dict": dict_user,
            "res": res}

@router.post("/user")
async def add_specific_users(new_user: User_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(user).values(**new_user.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "user added"}
