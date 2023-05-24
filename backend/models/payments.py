from pydantic import BaseModel
from .base import Base, OrmBase
from datetime import datetime


class PaymentBase(BaseModel):
    payment_code: str
    price: int
    tariff: str
    created_at: datetime


class PaymentModify(PaymentBase):
    pass


class Payment(PaymentBase, Base, OrmBase):
    pass
