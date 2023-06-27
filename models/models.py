from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey, TIMESTAMP
from datetime import datetime

metadata = MetaData()

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("email", String, nullable=False, unique=True),
    Column("tariff_id", Integer, ForeignKey("tariffs.id")),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)

tariffs = Table(
    "tariffs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("price", Float, nullable=False, unique=True),
    Column("description", String, nullable=False, unique=True),
    Column("server_id", Integer, ForeignKey("servers.id"))
)

hardwares = Table(
    "hardwares",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cpu", Float, nullable=False, unique=True),
    Column("capacity_of_ram", Float, nullable=False, unique=False),
    Column("capacity_of_disk", Float, nullable=False, unique=False),
    Column("status", String, nullable=False, unique=False)
)

servers = Table(
    "servers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("hardware_id", Integer, ForeignKey("hardwares.id")),
    Column("ip_address", String, nullable=False, unique=True),
    Column("operating_system", String, nullable=False, unique=False)
)

payments = Table(
    "payments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", Integer, ForeignKey("clients.id")),
    Column("tariff_id", Integer, ForeignKey("tariffs.id")),
    Column("price", String, nullable=False, unique=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)