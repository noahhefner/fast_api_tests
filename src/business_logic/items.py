from uuid import UUID
import src.models
import src.data_access
import sqlite3


def get_item_by_id(
    db: sqlite3.Connection,
    id: UUID,
) -> src.models.business.result.GetItemByID:
    """Get item by ID."""

    item: src.models.data_access.GetItemByID = (
        db,
        id,
    )

    return src.models.business.result.GetItemByID(
        id=data_access_result.id,
        name=data_access_result.name,
        quantity=data_access_result.quantity,
    )
