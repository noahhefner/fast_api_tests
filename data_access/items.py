import src.models


def get_item_by_id(
    db: sqlite3.Connection, data_access_model: src.models.data_access.call.GetItemByID
) -> src.models.data_access.result.GetItemByID:
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
