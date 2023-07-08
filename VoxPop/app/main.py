from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import CommentaryRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = CommentaryRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/comments")
def get_comments(request: Request, page: int = 1, limit: int = 5):
    comments = repository.get_all()

    total_comments = len(comments)
    total_pages = (total_comments - 1) // limit + 1
    start = (page - 1) * limit
    end = start + limit
    limited_comments = comments[start:end] 
    return templates.TemplateResponse(
        "comments/index.html",
        {
            "request": request,
            "comments": limited_comments,
            "page": page,
            "limit": limit,
            "total_comments": total_comments,
            "total_pages": total_pages,
        },
    )

@app.get("/comments/new")
def create_comment(request: Request):
    return templates.TemplateResponse(
        "comments/new.html",
        {"request": request}
    )

@app.post("/comments/new")
def create_comment(
    request: Request,
    text: str = Form(),
    category: str = Form(),
):
    repository.save(
        {
            "text": text,
            "category": category,
        }
    )

    return RedirectResponse("/comments", status_code=303)