import secrets
import os

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import extracker
print(extracker.d)

app = FastAPI()
security = HTTPBasic()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(
        credentials.username, os.getenv("USERNAME"))
    correct_password = secrets.compare_digest(
        credentials.password, os.getenv("PASSWORD"))
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/")
async def root(username: str = Depends(get_current_username)):
    return {"message": f'Hello, {username}'}


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request, username: str = Depends(get_current_username)):
    return templates.TemplateResponse("test.html", {"request": request, "user": username})


@app.get("/exercise", response_class=HTMLResponse)
async def about(request: Request, username: str = Depends(get_current_username)):
    return templates.TemplateResponse("ex.html", {"request": request, "user": username, "exercises": extracker.d})
