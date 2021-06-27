from decimal import Decimal
from typing import Set, Optional

from pydantic import BaseModel

# TODO-Pre-Workshop: Strip inheritance and properties


class ItemBase(BaseModel):
    # Properties: name, price, is_active, tags
    name: str
    price: Decimal
    is_active: bool
    tags: Optional[Set[str]]


class ItemOut(ItemBase):
    # Property: 'id'
    id: int
