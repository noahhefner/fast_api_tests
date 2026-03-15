from models.business.result.get_item_by_id import GetItemByID
from uuid import UUID
from fastapi import APIRouter, Depends

import src.business_logic
import src.models
from src.db import get_db

router = APIRouter()


@router.get(
    "/items/{id}",
    response_model=src.models.response.GetItemByID,
)
def get_item_by_id(
    id: UUID,
    db: sqlite3.Connection = Depends(get_db),
):

    # Create business model
    business_model: src.models.business.call.GetItemByID = (
        src.models.business.call.GetItemByID(id=id)
    )

    # Call business logic
    business_logic_result: src.models.business.result.GetItemByID = (
        src.business_logic.items.get_item_by_id(
            db,
            business_model,
        )
    )

    # Return data using response model
    return src.models.response.GetItemByID(
        id=business_logic_result.id,
        name=business_logic_result.name,
        quantity=business_logic_result.quantity,
    )
