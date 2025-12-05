from fastapi import FastAPI
from .routers import books
from .database import Base, engine

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 注册路由
app.include_router(books.router)

