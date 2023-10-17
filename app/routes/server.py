from app.models.models import server
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
# from app.auth.database import get_async_session
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

@router.post("/server/server_id_hardware_id_ip_address_operating_system")
async def add_specific_servers(server_id: int, hardware_id: int, ip_address: str, operating_system: int, session: AsyncSession = Depends(get_async_session)):
    vals = [server_id, hardware_id, ip_address, operating_system]
    stmt = insert(server).values(vals)
    await session.execute(stmt)
    await session.commit()
    query = select(server).where(server.c.id == server_id)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {
            "added_server": res
            }

@router.get("/server")
async def get_all_servers(session: AsyncSession = Depends(get_async_session)):
    query = select(server)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}



@router.post("/server/server_id")
async def find_server(server_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(server).where(server.c.id == server_id)
    result = await session.execute(query)
    res = []
    for el in result.all():
        res.append(el)
    return {"finded_server": res}

@router.post("/server/server_id")
async def delete_server(server_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(server).where(server.c.id == server_id)
    result = await session.execute(query)
    stmt = delete(server).where(server.c.id == server_id)
    await session.execute(stmt)
    await  session.commit()
    res = []
    for el in result.all():
        res.append(el)
    return {"res": res}