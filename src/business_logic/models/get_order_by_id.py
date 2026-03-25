from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class GetOrderByID(BaseModel):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    id: UUID
    address: str
    placed_on: datetime
