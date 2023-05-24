from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from backend import models
from backend.common.exceptions import CrudException, CrudNotFoundException
from backend.crud import CrudTariffs
from backend.dependencies import get_session, get_token_header


router = APIRouter(
    prefix='/tariffs',
    tags=['tariffs'],
    responses={
        404: {
            'description': 'Method not found'
        }
    }
)


@router.get('', response_model=List[models.Tariff])
async def get_all(session: Session = Depends(get_session)):
    return CrudTariffs.all(session)


@router.get('/{tariff_code}', response_model=models.Tariff)
async def get_by_id(tariff_code: str, session: Session = Depends(get_session)):
    item = CrudTariffs.one(session, tariff_code)
    if not item:
        raise HTTPException(status_code=404, detail=f'Tariff with code = {tariff_code} not found')
    return item


@router.post(
    '',
    tags=['tariffs_operation'],
    dependencies=[Depends(get_token_header)],
    status_code=201,
    response_model=models.Tariff,
)
async def create(tariff: models.TariffModify, session: Session = Depends(get_session)):
    try:
        item = CrudTariffs.create(session, tariff.dict())
        return item
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(
    '/{code}',
    tags=['tariffs_operation'],
    dependencies=[Depends(get_token_header)],
    response_model=models.Tariff
)
async def update(code: str, tariff: models.TariffModify, session: Session = Depends(get_session)):
    try:
        item = CrudTariffs.update(session, code, tariff.dict(exclude_unset=True))
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
        CrudTariffs.delete(session, code)
    except CrudNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
