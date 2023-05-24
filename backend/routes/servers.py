from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from backend import models
from backend.common.exceptions import CrudException, CrudNotFoundException
from backend.crud import CrudServers
from backend.dependencies import get_session, get_token_header


router = APIRouter(
    prefix='/servers',
    tags=['servers'],
    responses={
        404: {
            'description': 'Method not found'
        }
    }
)


@router.get('', response_model=List[models.Server])
async def get_all(session: Session = Depends(get_session)):
    return CrudServers.all(session)


@router.get('/{server_code}', response_model=models.Server)
async def get_by_id(server_code: str, session: Session = Depends(get_session)):
    item = CrudServers.one(session, server_code)
    if not item:
        raise HTTPException(status_code=404, detail=f'Server with code = {server_code} not found')
    return item


@router.post(
    '',
    tags=['servers_operation'],
    dependencies=[Depends(get_token_header)],
    status_code=201,
    response_model=models.Server,
)
async def create(server: models.ServerModify, session: Session = Depends(get_session)):
    try:
        item = CrudServers.create(session, server.dict())
        return item
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(
    '/{code}',
    tags=['servers_operation'],
    dependencies=[Depends(get_token_header)],
    response_model=models.Server
)
async def update(code: str, server: models.ServerModify, session: Session = Depends(get_session)):
    try:
        item = CrudServers.update(session, code, server.dict(exclude_unset=True))
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
        CrudServers.delete(session, code)
    except CrudNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CrudException as e:
        raise HTTPException(status_code=400, detail=str(e))
