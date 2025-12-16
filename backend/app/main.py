from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# 前端静态目录
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")

# 挂载静态资源（JS、CSS、图片）
# app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

app.mount(
    "/",  
    StaticFiles(directory=frontend_dir, html=True), # html=True 使得 StaticFiles 可以处理根目录的 index.html
    name="static_files"
)

# 访问根路径 -> 返回 index.html
@app.get("/")
def read_index():
    return FileResponse(os.path.join(frontend_dir, "index.html"), media_type='text/html')

@app.get("/add-book")
def add_book_page():
    return FileResponse(os.path.join(frontend_dir, "add-book.html"))

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    # 返回静态目录下的 index.html 文件
    return FileResponse(frontend_dir / "index.html", media_type="text/html")