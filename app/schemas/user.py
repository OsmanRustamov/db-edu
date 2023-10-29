from pydantic import BaseModel
from datetime import datetime
class User_create(BaseModel):
    id: int
    name: str
    email: str
    tariff_id: int
    created_at: datetime
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool