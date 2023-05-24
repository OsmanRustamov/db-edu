from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

class Clients(Base):
    __tablename__: str = 'clients'

    clients_code = Column(String(3), primary_key=True, index=True, comment='Код клиента', nullable=False)
    email = Column(String, nullable=False, index=True, unique=True, comment='Почта клиента')
    tariff = Column(String, nullable=False, index=True, unique=False, comment='Тариф клиента')
    created_at = Column(String, nullable=False, comment='Время добавления')

    @validates('email')
    def validate_distance(self, email: str) -> ValueError | str:
        if '@' not in email:
            raise ValueError('Enter valid email')
        return email
