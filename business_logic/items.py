import src.models
import src.data_access
import sqlite3


def get_item_by_id(
    db: sqlite3.Connection,
    business_model: src.models.business.call.GetItemByID,
) -> src.models.business.result.GetItemByID:
    """Get item by ID."""

    # Create data access model
    data_access_model: src.models.data_access.call.GetItemByID = (
        src.models.data_access.call.GetItemByID(id=business_model.id)
    )

    # Call data access function
    data_access_result: src.models.data_access.result.GetItemByID = (
        src.data_access.items.get_item_by_id(
            db=db,
            data_access_model=data_access_model,
        )
    )

    return src.models.business.result.GetItemByID(
        id=data_access_result.id,
        name=data_access_result.name,
        quantity=data_access_result.quantity,
    )
