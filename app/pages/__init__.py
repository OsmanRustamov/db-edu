from .user import router as user_router
from .hardware import router as hardware_router
from .tariff import router as tariff_router
from .server import router as server_router
from .payment import router as payment_router
from .main import router as main_router

routes = [
    main_router,
    user_router,
    hardware_router,
    tariff_router,
    server_router,
    payment_router
]

__all__ = ['routes']