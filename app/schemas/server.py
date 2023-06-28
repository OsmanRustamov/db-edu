from pydantic import BaseModel

class Server_create(BaseModel):
    id: int
    hardware_id: int
    ip_address: str
    operating_system: str