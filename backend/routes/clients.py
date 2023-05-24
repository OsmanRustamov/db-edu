from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from backend import models
from backend.common.exceptions import CrudException, CrudNotFoundException
from backend.crud import CrudClients
from backend.dependencies import get_session, get_token_header


router = APIRouter(
    prefix='/clients',
    tags=['clients'],
    responses={
        404: {
            'description': 'Method not found'
        }
    }
)


@router.get('', response_model=List[models.Client])
async def get_all(session: Session = Depends(get_session)):
    return CrudClients.all(session)


@router.get('/{client_code}', response_model=models.Client)
async def get_by_id(client_code: str, session: Session = Depends(get_session)):
    item = CrudClients.one(session, client_code)
    if not item:
        raise HTTPException(status_code=404, detail=f'Client with code = {client_code} not found')
    return item


@router.post(
    '',
    tags=['clients_operation'],
    dependencies=[Depends(get_token_header)],
    status_code=201,
    response_model=models.Client,
)
async def create(client: models.ClientModify, session: Session = Depends(get_session)):
    try:
        item = CrudClients.create(session, client.dict())
        return item
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(
    '/{code}',
    tags=['clients_operation'],
    dependencies=[Depends(get_token_header)],
    response_model=models.Client
)
async def update(code: str, client: models.ClientModify, session: Session = Depends(get_session)):
    try:
        item = CrudClients.update(session, code, client.dict(exclude_unset=True))
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
        CrudClients.delete(session, code)
    except CrudNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
