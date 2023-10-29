from .hardware import router as hardware_router
from .payment import router as payment_router
from .server import router as server_router
from .tariff import router as tariff_router
from .user import router as user_router

routes = (
    hardware_router,
    payment_router,
    server_router,
    tariff_router,
    user_router
)

__all__ = ['routes']