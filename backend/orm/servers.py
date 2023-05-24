from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


class Servers(Base):
    __tablename__: str = 'servers'

    server_code = Column(String(3), primary_key=True, index=True, comment='Код сервера', nullable=False)
    cpu = Column(String, nullable=False, index=True, unique=True, comment='Процессор')
    capacity_of_ram = Column(Integer, nullable=False, index=True, unique=True, comment='Количество оперативной памяти')
    capacity_of_disk = Column(Integer, nullable=False, index=True, unique=True, comment='Вместимость диска')
    os = Column(String, nullable=False, index=True, unique=False, comment='Операционная система')
    status = Column(String, nullable=False, index=True, unique=False, comment='статус сервера')

    @validates('capacity_of_ram')
    def validate_capacity_of_ram(self, capacity_of_ram: int) -> ValueError | int:
        if capacity_of_ram <= 0:
            raise ValueError('Capacity of RAM must have a value greater than 0')
        return capacity_of_ram

    @validates('capacity_of_disk')
    def validate_capacity_of_ram(self, capacity_of_disk: int) -> ValueError | int:
        if capacity_of_disk <= 0:
            raise ValueError('Capacity of Disk must have a value greater than 0')
        return capacity_of_disk
