from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.routes.tariff import get_all_tariffs
from app.routes.user import get_all_users, find_user
from app.routes.hardware import get_all_hardwares, find_hardware, add_hardware, delete_hardware


router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/auth")
def get_index(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@router.get("/main")
def get_main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})




