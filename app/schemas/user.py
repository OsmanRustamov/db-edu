from pydantic import BaseModel
from datetime import datetime
class User_create(BaseModel):
    id: int
    name: str
    email: str
    tariff_id: int
    hashed_password: str
    is_superuser: bool