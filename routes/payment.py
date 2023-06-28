from models.models import payment
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session
from schemas.payment import Payment_create

router = APIRouter(
    prefix='/payment',
    tags=['payment'],
)

@router.get("/payment/{payment_id}")
async def get_specific_payments(payment_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(payment).where(payment.c.id == payment_id)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_specific_payments(new_payment: Payment_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(payment).values(**new_payment.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "payment added"}
