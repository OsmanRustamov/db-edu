from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.routes.hardware import get_all_hardwares, find_hardware, add_hardware, delete_hardware


router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/hardware/hardwares")
def get_hardwares(request: Request):
    return templates.TemplateResponse("hardware/hardwares.html", {"request": request})

@router.get("/hardware/get_hardwares")
def get_all_hardwares(request: Request, hardware=Depends(get_all_hardwares)):
    return templates.TemplateResponse("hardware/get_hardwares.html", {"request": request, "hardware": hardware["res"]})

@router.post("/hardware/add_hardware")
async def add_hardware(request: Request, hardware=Depends(add_hardware)):
    return templates.TemplateResponse("hardware/add_hardware.html", {"request": request, "hardware": hardware["message"]})

@router.get("/hardware/find_hardware")
def find_hardwares(request: Request, hardware=Depends(find_hardware)):
    return templates.TemplateResponse("hardware/find_hardware.html", {"request": request, "hardware": hardware["finded_hardware"]})

@router.get("/hardware/delete_hardware")
def delete_hardwares(request: Request, hardware=Depends(delete_hardware)):
    return templates.TemplateResponse("hardware/delete_hardware.html", {"request": request, "hardware": hardware["message"]})
