from app.models.models import hardware
from fastapi import APIRouter, Depends, Body
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.schemas.hardware import Hardware_create

router = APIRouter(
    prefix='/hardware',
    tags=['hardware'],
)

@router.get("/hardware/{hardware_id}")
async def get_specific_hardwares(hardware_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(hardware).where(hardware.c.id == hardware_id)
    result = await session.execute(query)
    return result.all()

@router.post("/hardware")
async def add_specific_hardwares(new_hardware=Body(), session: AsyncSession = Depends(get_async_session)):
    stmt = insert(hardware).values(**new_hardware.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(hardware).where(hardware.c.id == new_hardware.dict().get("id"))
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}


@router.get("/hardware")
async def get_all_hardwares(session: AsyncSession = Depends(get_async_session)):
    query = select(hardware)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    print(res)
    return {"res": res}



@router.post("/hardware/hardware_id")
async def find_hardware(hardware_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(hardware).where(hardware.c.id == hardware_id)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"finded_hardware": res}

@router.post("/hardware/hardware_id")
async def delete_hardware(hardware_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(hardware).where(hardware.c.id == hardware_id)
    result = await session.execute(query)
    stmt = delete(hardware).where(hardware.c.id == hardware_id)
    await session.execute(stmt)
    await session.commit()
    return {"message": result}