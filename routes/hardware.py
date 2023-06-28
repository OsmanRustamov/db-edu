from models.models import hardware
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session
from schemas.hardware import Hardware_create

router = APIRouter(
    prefix='/hardware',
    tags=['hardware'],
)

@router.get("/hardware/{hardware_id}")
async def get_specific_hardwares(hardware_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(hardware).where(hardware.c.id == hardware_id)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_specific_hardwares(new_hardware: Hardware_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(hardware).values(**new_hardware.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "hardware added"}
