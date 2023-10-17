from app.models.models import payment
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
# from app.auth.database import get_async_session
from app.schemas.payment import Payment_create

router = APIRouter(
    prefix='/payment',
    tags=['payment'],
)

@router.get("/payment/{payment_id}")
async def get_specific_payments(payment_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(payment).where(payment.c.id == payment_id)
    result = await session.execute(query)
    return result.all()

@router.post("/payment")
async def add_specific_payments(new_payment: Payment_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(payment).values(**new_payment.dict())
    await session.execute(stmt)
    await  session.commit()
    query = select(payment).where(payment.c.id == new_payment.dict().get("id"))
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}

@router.get("/payment")
async def get_all_payments(session: AsyncSession = Depends(get_async_session)):
    query = select(payment)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    print(res)
    return {"res": res}

@router.post("/payment/payment_id")
async def find_payment(payment_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(payment).where(payment.c.id == payment_id)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"finded_payment": res}

@router.post("/payment/payment_id")
async def delete_payment(payment_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(payment).where(payment.c.id == payment_id)
    result = await session.execute(query)
    stmt = delete(payment).where(payment.c.id == payment_id)
    await session.execute(stmt)
    await session.commit()
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}