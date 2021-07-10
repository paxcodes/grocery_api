# PART 2 OF HOW-TO #3 CREATE AN ITEM: Create the "pydantic schema"
#
# As seen in the comments in "PART 1: Defining the endpoint"
# (in grocery_api/main.py), we need to create a "pydantic schema"
# to validate incoming data (data for the new item)
#
# To create a pydantic "schema", we use the `BaseModel` class which
# we import from `pydantic`.
from pydantic import BaseModel

# Import the `Decimal` class from python's `Decimal` package for
# type-hinting the `price` property
from decimal import Decimal

# Import the `Optional` and `Set` type from python's `typing` package
# for type-hinting the `tags` property
from typing import Optional, Set

# Specify BaseModel as the Item's parent class. This will make the regular
# python class into a "pydantic schema."
class Item(BaseModel):
    # Properties: name, price, is_active, tags (optional)
    #
    # Define the properties of Item and their data types.
    # Just like type-hinting our path parameters give data validation
    # out-of-the-box, using a pydantic schema and type-hinting
    # properties will also let FastAPI validate the data.
    name: str
    price: Decimal
    is_active: bool
    # This means that `tags` can be a value of "None" or
    # a set of strings. E.g. {"pantry", "organic"}
    tags: Optional[Set[str]]

# For PART 3: Go back to grocery_api/main.py and import the schema
