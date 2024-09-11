from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# get environment variables from .env file
load_dotenv()

from app.routers import product_router

app = FastAPI()


# ngăn chặn lỗi CORS.
# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

@app.get('/')
def greeting():
    return "Mysql API!"

app.include_router(product_router.router)


# uvicorn app.main:app --host 0.0.0.0 --port 5000