from uuid import UUID
import src.models.data_access as DataAccessModels
import src.models.data_access.errors as DataAccessErrors
import sqlite3


def get_item_by_id(
    db: sqlite3.Connection, id: UUID
) -> DataAccessModels.GetItemByID:
    """Fetch an item from the database by its ID."""

    try:
        cursor = db.execute(
            "SELECT id, name, quantity FROM items WHERE id = ?",
            (str(id),),
        )
        row = cursor.fetchone()
    except sqlite3.Error as e:
        raise DataAccessErrors.DatabaseError(str(e)) from e

    if row is None:
        raise DataAccessErrors.ItemNotFound(
            f"Failed to find item with id: {id}"
        )

    return DataAccessModels.GetItemByID.model_validate(row)