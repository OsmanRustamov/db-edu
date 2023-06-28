from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.routes.user import get_all_users
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
def get_users(request: Request):
    return templates.TemplateResponse("user/users.html", {"request": request})

@router.get("/user/get_users")
def get_users(request: Request, user=Depends(get_all_users)):
    return templates.TemplateResponse("user/get_users.html", {"request": request, "user": user["res"]})