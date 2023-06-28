from .hardwares import router as hardware_router
from .payments import router as payments_router
routes = (
    hardware_router,
    payments_router
)

__all__ = ['routes']