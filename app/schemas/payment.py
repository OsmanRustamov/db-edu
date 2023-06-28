from pydantic import BaseModel
from datetime import datetime
class Payment_create(BaseModel):
    id: int
    user_id: int
    tariff_id: int
    price: str
    created_at: datetime