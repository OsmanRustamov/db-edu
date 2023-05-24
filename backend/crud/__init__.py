
from .clients import Crud as CrudClients
from .payments import Crud as CrudPayments
from .servers import Crud as CrudServers
from .tariffs import Crud as CrudTariffs

__all__ = [
           'CrudClients',
           'CrudPayments',
           'CrudServers',
           'CrudTariffs'
           ]
