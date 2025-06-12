from fastapi import FastAPI
from app.auth import routes as auth_routes
from app.core.database import Base, engine
from app.auth.routes import router as auth_router
from app.admin.routes import router as admin_router
from app.products.routes import router as product_router
from app.cart.routes import router as cart_router
from app.orders.routes import router as order_router
from app.reset_token.routes import router as reset_token

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce Backend API",
    version="1.0.0"
)

# Include auth routes
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(reset_token)