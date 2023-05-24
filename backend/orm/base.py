import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Base(DeclarativeBase):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.datetime.utcnow, comment='Дата создания')
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, comment='Дата изменения')

    def fill(self, values: dict, on_empty: dict = None):
        for key, value in values.items():
            if hasattr(self, key):
                setattr(self, key, value)
        if not on_empty:
            return
        for key, value in on_empty.items():
            if hasattr(self, key) and not getattr(self, key):
                setattr(self, key, value)

