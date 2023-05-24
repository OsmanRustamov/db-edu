from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from backend import models
from backend.common.exceptions import CrudException, CrudNotFoundException
from backend.crud import CrudPayments
from backend.dependencies import get_session, get_token_header


router = APIRouter(
    prefix='/payments',
    tags=['payments'],
    responses={
        404: {
            'description': 'Method not found'
        }
    }
)


@router.get('', response_model=List[models.Payment])
async def get_all(session: Session = Depends(get_session)):
    return CrudPayments.all(session)


@router.get('/{payment_code}', response_model=models.Payment)
async def get_by_id(payment_code: str, session: Session = Depends(get_session)):
    item = CrudPayments.one(session, payment_code)
    if not item:
        raise HTTPException(status_code=404, detail=f'Payment with code = {payment_code} not found')
    return item


@router.post(
    '',
    tags=['payments_operation'],
    dependencies=[Depends(get_token_header)],
    status_code=201,
    response_model=models.Payment,
)
async def create(payment: models.PaymentModify, session: Session = Depends(get_session)):
    try:
        item = CrudPayments.create(session, payment.dict())
        return item
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(
    '/{code}',
    tags=['payments_operation'],
    dependencies=[Depends(get_token_header)],
    response_model=models.Payment
)
async def update(code: str, payment: models.PaymentModify, session: Session = Depends(get_session)):
    try:
        item = CrudPayments.update(session, code, payment.dict(exclude_unset=True))
        return item
    except CrudNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(
    '/{code}',
    tags=['classes_operation'],
    status_code=204,
    dependencies=[Depends(get_token_header)]
)
async def delete(code: str, session: Session = Depends(get_session)):
    try:
        CrudPayments.delete(session, code)
    except CrudNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
