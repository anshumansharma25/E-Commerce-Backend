from fastapi import Depends, HTTPException, status
from app.auth import models
from app.auth.token import get_current_user


# Only allow admins
def require_admin(current_user: models.User = Depends(get_current_user)) -> models.User:
    if current_user.role != models.UserRole.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


# Allow only regular users
def require_user(current_user: models.User = Depends(get_current_user)) -> models.User:
    if current_user.role != models.UserRole.user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User access required"
        )
    return current_user
