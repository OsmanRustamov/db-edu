from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class OrmBase(BaseModel):
    class Config:
        orm_mode = True
