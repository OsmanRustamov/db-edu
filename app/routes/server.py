from app.models.models import server
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.schemas.server import Server_create

router = APIRouter(
    prefix='/server',
    tags=['server'],
)

@router.get("/server/{server_id}")
async def get_specific_servers(server_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(server).where(server.c.id == server_id)
    result = await session.execute(query)
    return result.all()

@router.post("/server")
async def add_specific_servers(new_server: Server_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(server).values(**new_server.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "server added"}

@router.get("/server")
async def get_all_servers(session: AsyncSession = Depends(get_async_session)):
    query = select(server)
    result = await session.execute(query)
    dict_server = dict()
    res = []
    for el in result.all():
        dict_server.update({"id": el[0]})
        dict_server.update({"cpu": el[1]})
        dict_server.update({"capacity_of_ram": el[2]})
        dict_server.update({"capacity_of_disk": el[3]})
        dict_server.update({"status": el[4]})
        res.append(el)
    return {"res": res}



@router.post("/server/server_id")
async def find_server(server_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(server).where(server.c.id == server_id)
    result = await session.execute(query)
    dict_server = dict()
    res = []
    for el in result.all():
        dict_server.update({"id": el[0]})
        dict_server.update({"cpu": el[1]})
        dict_server.update({"capacity_of_ram": el[2]})
        dict_server.update({"capacity_of_disk": el[3]})
        dict_server.update({"status": el[4]})
        res.append(el)
    return {"finded_server": res}

@router.post("/server/server_id")
async def delete_server(server_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(server).where(server.c.id == server_id)
    await session.execute(stmt)
    await  session.commit()
    res = []
    for el in stmt.all():
        res.append(el)
    return {"res": res}