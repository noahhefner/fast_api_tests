from uuid import UUID
import src.models.business as BusinessModels
import src.models.data_access.errors as DataAccessErrors
import src.models.data_access as DataAccessModels
import src.data_access.items as DataAccessItems
import sqlite3
import src.models.business.errors as BusinessLogicErrors

def get_item_by_id(
    db: sqlite3.Connection,
    id: UUID,
) -> BusinessModels.GetItemByID:
    """Get item by ID."""

    try:
        item: DataAccessModels.GetItemByID = DataAccessItems.get_item_by_id(
            db,
            id,
        )
    except DataAccessErrors.DatabaseError as e:
        raise BusinessLogicErrors.DatabaseError(str(e)) from e
    except DataAccessErrors.ItemNotFound as e:
        raise BusinessLogicErrors.ItemNotFound(str(e)) from e

    return BusinessModels.GetItemByID.model_validate(item)
