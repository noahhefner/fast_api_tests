from uuid import UUID
import src.models.data_access as DataAccessModels
import src.models.data_access.errors as DataAccessErrors
import sqlite3

def get_item_by_id(
    db: sqlite3.Connection, id: UUID
) -> DataAccessModels.GetItemByID:
    """Get an item from the database by ID."""

    cursor = db.execute(
        "SELECT id, name, quantity FROM items WHERE id = ?", (id,)
    )

    row = cursor.fetchone()

    if row is None:
        raise DataAccessErrors.ItemNotFound(f"Failed to find item with id: {str(id)}")

    return DataAccessModels.GetItemByID(
        id=row["id"],
        name=row["name"],
        quantity=row["quantity"],
    )