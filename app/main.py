from app.api.routes import auth, role_protected
from fastapi import FastAPI
from app.api.routes import auth, inventory,  shelf, staff_assignment
from app.database.db import engine, Base
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShelfCam API",
    description="AI-Powered Retail Shelf Monitoring System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "ShelfCam API is live!"}

app.include_router(auth.router)
app.include_router(inventory.router)
app.include_router(shelf.router)
app.include_router(staff_assignment.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
