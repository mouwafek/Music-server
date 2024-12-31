from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routes import auth

from models.base import Base

from database import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix='/auth')

Base.metadata.create_all(engine)