from uuid import UUID
import src.models.business as BusinessModels
import src.models.data_access as DataAccessModels
import src.data_access.items as DataAccessItems
import sqlite3


def get_item_by_id(
    db: sqlite3.Connection,
    id: UUID,
) -> BusinessModels.GetItemByID:
    """Get item by ID."""

    item: DataAccessModels.GetItemByID = DataAccessItems.get_item_by_id(
        db,
        id,
    )

    return BusinessModels.GetItemByID(
        id=item.id,
        name=item.name,
        quantity=item.quantity,
    )
