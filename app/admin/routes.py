from fastapi import APIRouter, Depends
from app.auth.dependencies import require_admin

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(require_admin)]
)


@router.get("/dashboard")
def admin_dashboard():
    return {"message": "Admin access granted!"}
