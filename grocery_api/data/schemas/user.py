from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    email: str
    username: str


class UserSensitiveData(UserBase):
    id: UUID4
    sh_password: str
    salt: str


class UserOut(UserBase):
    id: UUID4
