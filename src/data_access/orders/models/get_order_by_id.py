from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class GetOrderByID(BaseModel):
    id: UUID
    address: str
    placed_on: datetime
