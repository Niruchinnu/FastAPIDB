from fastapi import FastAPI
from .routers import users
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with MySQL!"}