# PART 2 OF EXERCISE #3 CREATE A STORE: Create the "pydantic schema."
from typing import Optional
from pydantic import BaseModel


class Store(BaseModel):
    # Properties: name (a string), founding_year (an integer),
    # is_active (a boolean), parent_company (an optional string)
    name: str
    founding_year: int
    is_active: bool
    parent_company: Optional[str]

# For PART 3: Go back to grocery_api/main.py and import the schema
