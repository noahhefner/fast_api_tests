from uuid import UUID
from pydantic import BaseModel


class GetItemByIDBusinessModel(BaseModel):
    id: UUID
