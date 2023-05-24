from pydantic import BaseModel
from .base import Base, OrmBase


class ServerBase(BaseModel):
    server_code: str
    cpu: str
    capacity_of_ram: int
    capacity_of_disk: int
    os: str
    status: str


class ServerModify(ServerBase):
    pass


class Server(ServerBase, Base, OrmBase):
    pass
