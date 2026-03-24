import sqlite3
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

import src.business_logic.domains.items as ItemsBusinessLogic
import src.business_logic.errors as BusinessErrors
import src.business_logic.models as BusinessModels
import src.routers.response_models as ResponseModels
from src.db import get_db

router = APIRouter()


@router.get("/{id}", response_model=ResponseModels.GetItemByID)
def get_item_by_id(id: UUID, db: sqlite3.Connection = Depends(get_db)):
    """
    Retrieves an item by ID and converts domain errors into appropriate HTTP
    responses.
    """
    try:
        item: BusinessModels.GetItemByID = ItemsBusinessLogic.get_item_by_id(
            db,
            id,
        )
    except BusinessErrors.DatabaseError as e:
        print(str(e))
        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        )
    except BusinessErrors.ItemNotFound:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    return item
