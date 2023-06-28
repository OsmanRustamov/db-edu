from pydantic import BaseModel

class Tariff_create(BaseModel):
    id: int
    price: str
    description: str
    server_id: int