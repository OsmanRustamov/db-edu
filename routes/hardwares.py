from models.models import hardware
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session


router = APIRouter(
    prefix='/hardware',
    tags=['hardware'],
)

@router.get("/")
async def get_hardware(hardware_status: str, session: AsyncSession = Depends(get_async_session)):
    query = select(hardware).where(hardware.c.status == hardware_status)
    print(query)
    result = await session.execute(query)
    return result.all()
