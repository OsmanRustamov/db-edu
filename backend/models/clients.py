from pydantic import BaseModel
from .base import Base, OrmBase
from datetime import datetime


class ClientBase(BaseModel):
    client_code: str
    email: str
    tariff: str
    created_at: datetime


class ClientModify(ClientBase):
    pass


class Client(ClientBase, Base, OrmBase):
    pass
