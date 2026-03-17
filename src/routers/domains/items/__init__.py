from fastapi import APIRouter

from . import get_item_by_id

router = APIRouter(prefix="/items", tags=["items"])

router.include_router(get_item_by_id.router)
