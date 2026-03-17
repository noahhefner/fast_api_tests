import sqlite3
from uuid import UUID

import src.business_logic.errors as BusinessLogicErrors
import src.business_logic.models as BusinessModels
import src.data_access.domains.items as ItemsDataAccess
import src.data_access.errors as DataAccessErrors
import src.data_access.models as ItemDataAccessModels


def get_item_by_id(
    db: sqlite3.Connection,
    id: UUID,
) -> BusinessModels.GetItemByID:
    """
    Retrieves an item by ID, translating data access errors and returning a
    business model.
    """
    try:
        item: ItemDataAccessModels.GetItemByID = ItemsDataAccess.get_item_by_id(
            db,
            id,
        )
    except DataAccessErrors.DatabaseError as e:
        raise BusinessLogicErrors.DatabaseError(str(e)) from e
    except DataAccessErrors.ItemNotFound as e:
        raise BusinessLogicErrors.ItemNotFound(str(e)) from e

    return BusinessModels.GetItemByID.model_validate(item)
