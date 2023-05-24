from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


class Tariffs(Base):
    __tablename__: str = 'tariffs'

    tariff_code = Column(String(3), primary_key=True, index=True, comment='Код тарифа', nullable=False)
    price = Column(Integer, nullable=False, index=True, unique=True, comment='Цена тарифа')
    type_name = Column(String, nullable=False, index=True, unique=True, comment='Описание тарифа')
    server = Column(String, nullable=False, index=True, unique=True, comment='Выделенный сервер')


    @validates('price')
    def validate_price(self, price: int) -> ValueError | int:
        if price <= 0:
            raise ValueError('Price must have a value greater than 0')
        return price

