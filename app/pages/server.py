from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.routes.tariff import get_all_tariffs
from app.routes.user import get_all_users, find_user
from app.routes.server import get_all_servers, find_server, add_specific_servers, delete_server


router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")


from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.routes.server import get_all_servers, find_server, add_specific_servers, delete_server


router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/server/servers")
def get_servers(request: Request):
    return templates.TemplateResponse("server/servers.html", {"request": request})

@router.get("/server/get_servers")
def get_all_servers(request: Request, server=Depends(get_all_servers)):
    return templates.TemplateResponse("server/get_servers.html", {"request": request, "server": server["res"]})

@router.post("/server/add_server")
async def add_server(request: Request, server=Depends(add_specific_servers)):
    return templates.TemplateResponse("server/add_server.html", {"request": request, "server": server["status"]})

@router.get("/server/find_server")
def find_servers(request: Request, server=Depends(find_server)):
    return templates.TemplateResponse("server/find_server.html", {"request": request, "server": server["finded_server"]})

@router.get("/server/delete_server")
def delete_servers(request: Request, server=Depends(delete_server)):
    return templates.TemplateResponse("server/delete_server.html", {"request": request, "server": server["res"]})
