from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.routes.user import get_all_users, find_user, delete_user


router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/user/users")
def get_user(request: Request):
    return templates.TemplateResponse("user/users.html", {"request": request})

@router.get("/user/get_users")
def get_all_users(request: Request, user=Depends(get_all_users)):
    return templates.TemplateResponse("user/get_users.html", {"request": request, "user": user["res"]})

@router.get("/user/find_user")
def find_user(request: Request, user=Depends(find_user)):
    return templates.TemplateResponse("user/find_user.html", {"request": request, "user": user["finded_user"]})

@router.get("/user/delete_user")
def delete_user(request: Request, user=Depends(delete_user)):
    return templates.TemplateResponse("user/delete_user.html", {"request": request, "user": user["res"]})
