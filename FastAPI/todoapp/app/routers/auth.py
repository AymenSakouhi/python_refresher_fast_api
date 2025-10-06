"""Everything protected here"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/auth/")
async def get_user():
    """User auth route example"""
    return {"user": "Aymen"}
