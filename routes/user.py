from models.models import user
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session
from schemas.user import User_create

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.get("/user/{user_id}")
async def get_specific_users(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(user).where(user.c.id == user_id)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_specific_users(new_user: User_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(user).values(**new_user.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "user added"}
