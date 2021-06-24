from decimal import Decimal
from typing import Set, Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: Decimal
    is_active: bool
    tags: Optional[Set[str]]
