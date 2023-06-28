from pydantic import BaseModel

class Hardware_create(BaseModel):
    id: int
    cpu: str
    capacity_of_ram: str
    capacity_of_disk: str
    status: str