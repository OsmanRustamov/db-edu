from models.models import tariff
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session
from schemas.tariff import Tariff_create

router = APIRouter(
    prefix='/tariff',
    tags=['tariff'],
)

@router.get("/tariff/{tariff_id}")
async def get_specific_tariffs(tariff_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(tariff).where(tariff.c.id == tariff_id)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_specific_tariffs(new_tariff: Tariff_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(tariff).values(**new_tariff.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "tariff added"}
