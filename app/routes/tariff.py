from app.models.models import tariff
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
# from app.auth.database import get_async_session
from app.schemas.tariff import Tariff_create

router = APIRouter(
    prefix='/tariff',
    tags=['tariff'],
)

@router.post("/tariff")
async def add_specific_tariff(new_tariff: Tariff_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(tariff).values(**new_tariff.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "tariff added"}


@router.get("/tariff")
async def get_all_tariffs(session: AsyncSession = Depends(get_async_session)):
    query = select(tariff)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}



@router.post("/tariff/tariff_id")
async def find_tariff(tariff_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(tariff).where(tariff.c.id == tariff_id)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"finded_tariff": res}

@router.post("/tariff/tariff_id")
async def delete_tariff(tariff_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(tariff).where(tariff.c.id == tariff_id)
    result = await session.execute(query)
    stmt = delete(tariff).where(tariff.c.id == tariff_id)
    await session.execute(stmt)
    await  session.commit()
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}