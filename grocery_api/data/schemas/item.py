from decimal import Decimal
from typing import Set, Optional

from pydantic import BaseModel

# TODO-Pre-Workshop: Strip properties


class ItemBase(BaseModel):
    # TODO: Add properties: name, price, is_active, tags
    name: str
    price: Decimal
    is_active: bool
    tags: Optional[Set[str]]


class ItemOut(ItemBase):
    # TODO: Add property: 'id'
    id: int
