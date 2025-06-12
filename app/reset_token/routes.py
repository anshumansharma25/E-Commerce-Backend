from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import uuid
from app.core.database import get_db
from app.auth.models import User
from app.reset_token.models import  PasswordResetToken
from app.reset_token.schemas import ForgotPasswordRequest
from app.utils.email import send_reset_email
from app.reset_token.schemas import ResetPasswordRequest
from app.auth.utils import hash_password

router = APIRouter(
    prefix="",
    tags=["Reset Token"],
)


@router.post("/auth/forgot-password")
def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")

    token = str(uuid.uuid4())
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    db_token = PasswordResetToken(
        user_id=user.id,
        token=token,
        expiration_time=expiration_time
    )
    db.add(db_token)
    db.commit()

    send_reset_email(user.email, token)
    return {"message": "Password reset link sent to your email"}


@router.post("/auth/reset-password")
def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    db_token = db.query(PasswordResetToken).filter_by(token=request.token).first()

    if not db_token or db_token.used or db_token.expiration_time < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = db.query(User).filter_by(id=db_token.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.hashed_password = hash_password(request.new_password)
    db_token.used = True

    db.commit()
    return {"message": "Password reset successful"}
