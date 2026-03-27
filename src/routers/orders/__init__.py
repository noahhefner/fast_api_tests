from fastapi import APIRouter

from . import get_order_by_id

router = APIRouter(prefix="/api/orders", tags=["orders"])

router.include_router(get_order_by_id.router)
