from uuid import UUID
import src.models


def get_item_by_id(
    db: sqlite3.Connection, id: UUID
) -> src.models.data_access.result.GetItemByID | None:
    """Get an item from the database by ID."""

    cursor = db.execute(
        "SELECT id, name, quantity FROM items WHERE id = ?", (data_access_model.id,)
    )

    row = cursor.fetchone()

    if row:
        return src.models.data_access.result.GetItemByID(
            id=row["id"],
            name=row["name"],
            quantity=row["quantity"],
        )

    return None
