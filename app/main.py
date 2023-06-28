from fastapi import FastAPI, Depends
import uvicorn

from fastapi_users import FastAPIUsers

from app.auth.auth import auth_backend
from app.auth.database import User
from app.auth.manager import get_user_manager
from app.auth.schemas import UserRead, UserCreate
from app.routes import routes
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

app.include_router(router_pages)
for route in routes:
    app.include_router(route)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5433, reload=True, workers=3)