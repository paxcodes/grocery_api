from typing import Optional
from pydantic import BaseModel

# TODO-Pre-Workshop: Strip inheritance and properties


class StoreBase(BaseModel):
    # Properties: name, founding_year, is_active, parent_company
    name: str
    founding_year: int
    is_active: bool
    parent_company: Optional[str]


class StoreOut(StoreBase):
    # Property: id
    id: int
