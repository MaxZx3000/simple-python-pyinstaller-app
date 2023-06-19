from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sources import calc

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

@app.get("/", response_class = HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("response.html", context = {"request": request})

@app.post("/", response_class = HTMLResponse)
async def get_result_page(request: Request, num1: int = Form(...), num2: int = Form(...)):
    result = calc.add2(num1, num2)
    return templates.TemplateResponse("response.html", context = {"request": request, "result": result})