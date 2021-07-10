from pydantic import BaseModel, UUID4

# Just like the pydantic schema we have for Item and Store,
# UserOut inherits from BaseModel.
#
# This is the schema we want to use when returning user data.
# Notice that it only contains non-sensitive info and sensitive info
# such as "password" and "salt" are not included.
class UserOut(BaseModel):
    id: UUID4
    email: str
    username: str
