from .clients import router as clients_router
from .servers import router as servers_router
from .payments import router as payments_router
from .tariffs import router as tariffs_router

routes = (
    clients_router,
    servers_router,
    payments_router,
    tariffs_router
)

__all__ = ['routes']
