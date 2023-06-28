from models.models import server
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session
from schemas.server import Server_create

router = APIRouter(
    prefix='/server',
    tags=['server'],
)

@router.get("/server/{server_id}")
async def get_specific_servers(server_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(server).where(server.c.id == server_id)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_specific_servers(new_server: Server_create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(server).values(**new_server.dict())
    await session.execute(stmt)
    await  session.commit()
    return {"status": "server added"}
