from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# 前端静态目录
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")

# 挂载静态资源（JS、CSS、图片）
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

# 访问根路径 -> 返回 index.html
@app.get("/")
def read_index():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

@app.get("/add-book")
def add_book_page():
    return FileResponse(os.path.join(frontend_dir, "add-book.html"))

