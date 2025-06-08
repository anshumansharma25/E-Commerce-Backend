from fastapi import FastAPI
from app.auth import routes as auth_routes
from app.core.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce Backend API",
    version="1.0.0"
)

# Include auth routes
app.include_router(auth_routes.router)
