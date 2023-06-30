from fastapi import APIRouter, Request, Depends, Body
from fastapi.templating import Jinja2Templates
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import hardware

from app.auth.database import get_async_session
from app.routes.user import get_all_users, find_user
from app.routes.hardware import get_all_hardwares, find_hardware, add_specific_hardwares, delete_hardware
from app.schemas.hardware import Hardware_create

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

@router.get("/user/users")
def get_user(request: Request):
    return templates.TemplateResponse("user/users.html", {"request": request})

@router.get("/user/get_users")
def get_all_users(request: Request, user=Depends(get_all_users)):
    return templates.TemplateResponse("user/get_users.html", {"request": request, "user": user["res"]})

@router.get("/user/find_user")
def find_user(request: Request, user=Depends(find_user)):
    return templates.TemplateResponse("user/find_user.html", {"request": request, "user": user["finded_user"]})

@router.get("/hardware/hardwares")
def get_hardwares(request: Request):
    return templates.TemplateResponse("hardware/hardwares.html", {"request": request})

@router.get("/hardware/get_hardwares")
def get_all_hardwares(request: Request, hardware=Depends(get_all_hardwares)):
    return templates.TemplateResponse("hardware/get_hardwares.html", {"request": request, "hardware": hardware["res"]})

@router.post("/hardware/add_hardware")
async def add_hardware(request: Request):
    return templates.TemplateResponse("hardware/add_hardware.html", {"request": request})

@router.get("/hardware/find_hardware")
def find_hardwares(request: Request, hardware=Depends(find_hardware)):
    return templates.TemplateResponse("hardware/find_hardware.html", {"request": request, "hardware": hardware["finded_hardware"]})

@router.get("/hardware/delete_hardware")
def find_hardwares(request: Request, hardware=Depends(delete_hardware)):
    return templates.TemplateResponse("hardware/delete_hardware.html", {"request": request, "hardware": hardware["message"]})