# Quick Reference for the Workshop

## HTTP Methods

POST: to create an API resource.
GET: to read an API resource.
PUT*: to update an API resource with a complete resource representation (e.g. completely replace it).
PATCH*: to partially update an API resource (e.g. modify one of the fields)
DELETE: to delete data.

* PATCH is less commonly used and known than PUT. Many teams also use PUT for partial updates.

## Python Types

These are types relevant for the workshop. It is not an exhaustive list.

Built-in types: `str`, `int`, `bool`

From the `typing` package: 

- `Optional` (e.g. `Optional[str]` - an optional string; can be an instance of a string or `None`)
- `List` (e.g. `List[Item]` - a list of `Item` instances)

From the other packages in the standard library: 

- `from enum import Enum` - Limit the variable to predefined values
- `from decimal import Decimal` - When precision is important (e.g. prices)

Pydantic Types ([docs](https://pydantic-docs.helpmanual.io/usage/types/))

- Email addresses (`EmailStr`) - requires [email-validator](https://github.com/JoshData/python-email-validator) to be installed as mentioned in the pydantic [docs](https://pydantic-docs.helpmanual.io/usage/types/).

Other types from the `typing` package commonly used: 

- `Union` (e.g. `Union[int, str]` - can be either an `int` or `str`)
- `Literal` (e.g. `Literal["Hello World!"]` - it is always the literal string `Hello World!`)
- `Final` (e.g. `Final[int]` - The variable is an `int` and cannot be re-assigned or overridden in a subclass)