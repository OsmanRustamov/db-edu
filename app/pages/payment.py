from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.routes.tariff import get_all_tariffs
from app.routes.user import get_all_users, find_user
from app.routes.payment import get_all_payments, find_payment, add_specific_payments, delete_payment


router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/payment/payments")
def get_payments(request: Request):
    return templates.TemplateResponse("payment/payments.html", {"request": request})

@router.get("/payment/get_payments")
def get_all_payments(request: Request, payment=Depends(get_all_payments)):
    return templates.TemplateResponse("payment/get_payments.html", {"request": request, "payment": payment["res"]})

@router.post("/payment/add_payment")
async def add_payment(request: Request, payment=Depends(add_specific_payments)):
    return templates.TemplateResponse("payment/add_payment.html", {"request": request, "payment": payment["res"]})

@router.get("/payment/find_payment")
def find_payments(request: Request, payment=Depends(find_payment)):
    return templates.TemplateResponse("payment/find_payment.html", {"request": request, "payment": payment["finded_payment"]})

@router.get("/payment/delete_payment")
def delete_payments(request: Request, payment=Depends(delete_payment)):
    return templates.TemplateResponse("payment/delete_payment.html", {"request": request, "payment": payment["res"]})
