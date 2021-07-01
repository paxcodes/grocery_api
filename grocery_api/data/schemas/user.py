from pydantic import BaseModel, UUID4


class UserOut(BaseModel):
    id: UUID4
    email: str
    username: str
