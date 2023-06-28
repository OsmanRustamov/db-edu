from sqlalchemy import Table, Column, String, Integer, String, MetaData, ForeignKey, TIMESTAMP, Boolean
from datetime import datetime

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("email", String, nullable=False, unique=True),
    Column("tariff_id", Integer, ForeignKey("tariff.id"), nullable=True),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

tariff = Table(
    "tariff",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("price", String, nullable=False, unique=True),
    Column("description", String, nullable=False, unique=True),
    Column("server_id", Integer, ForeignKey("server.id"))
)

hardware = Table(
    "hardware",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cpu", String, nullable=False, unique=True),
    Column("capacity_of_ram", String, nullable=False, unique=False),
    Column("capacity_of_disk", String, nullable=False, unique=False),
    Column("status", String, nullable=False, unique=False)
)

server = Table(
    "server",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("hardware_id", Integer, ForeignKey("hardware.id")),
    Column("ip_address", String, nullable=False, unique=True),
    Column("operating_system", String, nullable=False, unique=False)
)

payment = Table(
    "payment",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("tariff_id", Integer, ForeignKey("tariff.id")),
    Column("price", String, nullable=False, unique=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)
