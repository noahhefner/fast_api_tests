import sqlite3
from uuid import UUID

import src.business_logic.errors as CommonBusinessLogicErrors
import src.business_logic.orders.errors as BusinessLogicErrors
import src.business_logic.orders.models as BusinessModels
import src.data_access.errors as CommonDataAccessErrors
import src.data_access.orders as DataAccess
import src.data_access.orders.errors as DataAccessErrors
import src.data_access.orders.models as DataAccessModels


def get_order_by_id(
    db: sqlite3.Connection,
    id: UUID,
) -> BusinessModels.GetOrderByID:
    """
    Retrieves an order by ID, translating data access errors and returning a
    business model.
    """
    try:
        order: DataAccessModels.GetOrderByID = DataAccess.get_order_by_id(
            db,
            id,
        )
    except CommonDataAccessErrors.DatabaseError as e:
        raise CommonBusinessLogicErrors.DatabaseError(str(e)) from e
    except DataAccessErrors.OrderNotFound as e:
        raise BusinessLogicErrors.OrderNotFound(str(e)) from e

    return BusinessModels.GetOrderByID.model_validate(order)
