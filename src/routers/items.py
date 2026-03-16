import sqlite3
from uuid import UUID
from fastapi import APIRouter, Depends

import src.business_logic
import src.models.response as ResponeModels
import src.models.business as BusinessModels
from src.db import get_db

router = APIRouter()


@router.get(
    "/items/{id}",
    response_model=ResponeModels.GetItemByID,
)
def get_item_by_id(
    id: UUID,
    db: sqlite3.Connection = Depends(get_db),
):
    """Get item by ID."""

    # Call business logic
    item: BusinessModels.GetItemByID = (
        db,
        id,
    )

    return item
