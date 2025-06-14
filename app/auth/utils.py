from passlib.context import CryptContext

# bcrypt is a hashing algorithm specifically designed for passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash the plain password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Check if the entered password matches the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)
