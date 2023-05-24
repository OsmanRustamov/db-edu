from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


class Payments(Base):
    __tablename__: str = 'payments'

    payments_code = Column(String(3), primary_key=True, index=True, comment='Код оплаты', nullable=False)
    price = Column(Integer, nullable=False, index=True, unique=False, comment='Цена')
    tariff = Column(String, nullable=False, index=True, unique=False, comment='Выбранный тариф')
    created_at = Column(Integer, nullable=False, index=True, unique=False, comment='Время создания')


    @validates('price')
    def validate_price(self, price: int) -> ValueError | int:
        if price <= 0:
            raise ValueError('Price must have a value greater than 0')
        return price