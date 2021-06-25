from decimal import Decimal
from typing import Set, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: Decimal
    is_active: bool
    tags: Optional[Set[str]]


class ItemOut(ItemBase):
    # TODO: Add 'id' property
    pass
