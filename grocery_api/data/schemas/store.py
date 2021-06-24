from pydantic import BaseModel


class Store(BaseModel):
    id: int
    name: str
    founding_year: int
    is_active: bool
