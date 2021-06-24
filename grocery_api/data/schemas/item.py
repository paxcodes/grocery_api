from decimal import Decimal
from typing import Set

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: Decimal
    is_active: bool
    tags: Set[str]
