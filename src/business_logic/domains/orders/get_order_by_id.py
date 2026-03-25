import sqlite3
from uuid import UUID

import src.business_logic.errors as BusinessLogicErrors
import src.business_logic.models as BusinessModels
import src.data_access.domains.orders as OrdersDataAccess
import src.data_access.errors as DataAccessErrors
import src.data_access.models as DataAccessModels


def get_order_by_id(
    db: sqlite3.Connection,
    id: UUID,
) -> BusinessModels.GetOrderByID:
    """
    Retrieves an order by ID, translating data access errors and returning a
    business model.
    """
    try:
        order: DataAccessModels.GetOrderByID = OrdersDataAccess.get_order_by_id(
            db,
            id,
        )
    except DataAccessErrors.DatabaseError as e:
        raise BusinessLogicErrors.DatabaseError(str(e)) from e
    except DataAccessErrors.OrderNotFound as e:
        raise BusinessLogicErrors.ItemNotFound(str(e)) from e

    return BusinessModels.GetOrderByID.model_validate(order)
