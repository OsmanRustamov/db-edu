from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.routes.tariff import get_all_tariffs, add_specific_tariff, find_tariff, delete_tariff

router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/tariff/tariffs")
def get_tariff(request: Request):
    return templates.TemplateResponse("tariff/tariffs.html", {"request": request})

@router.get("/tariff/get_tariffs")
def get_all_tariffs(request: Request, tariff=Depends(get_all_tariffs)):
    return templates.TemplateResponse("tariff/get_tariffs.html", {"request": request, "tariff": tariff["res"]})

@router.post("/tariff/add_tariff")
async def add_tariff(request: Request, tariff=Depends(add_specific_tariff)):
    return templates.TemplateResponse("tariff/add_tariff.html", {"request": request, "tariff": tariff["status"]})

@router.get("/tariff/find_tariff")
def find_tariff(request: Request, tariff=Depends(find_tariff)):
    return templates.TemplateResponse("tariff/find_tariff.html", {"request": request, "tariff": tariff["finded_tariff"]})

@router.get("/tariff/delete_tariff")
def delete_tariff(request: Request, tariff=Depends(delete_tariff)):
    return templates.TemplateResponse("tariff/delete_tariff.html", {"request": request, "tariff": tariff["res"]})
