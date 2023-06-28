from models.models import payment
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session


router = APIRouter(
    prefix='/payment',
    tags=['payment'],
)

@router.get("/")
async def get_payment(payment_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(payment).where(payment.c.id == payment_id)
    result = await session.execute(query)
    return result.all()