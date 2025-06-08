import os
from dotenv import load_dotenv

# Load environment variables from .env file into system environment
load_dotenv()


class Settings:
    PROJECT_NAME: str = "E-commerce API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ecommerce.db")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes token validity


# Create an instance of settings that can be imported elsewhere
settings = Settings()
