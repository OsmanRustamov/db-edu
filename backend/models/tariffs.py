from pydantic import BaseModel
from .base import Base, OrmBase


class TariffBase(BaseModel):
    server_code: str
    price: int
    type_name: str
    server: str


class TariffModify(TariffBase):
    pass


class Tariff(TariffBase, Base, OrmBase):
    pass
