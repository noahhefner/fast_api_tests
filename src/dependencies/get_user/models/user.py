from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    """User information."""

    id: UUID
    username: str
    display_name: str
