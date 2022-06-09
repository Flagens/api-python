from pydantic import BaseModel, constr


class Room(BaseModel):
    name: constr(min_length=2, max_length=50)
    beds: int
    price: float




class ListRoom(BaseModel):
    id: int
    name: str


    class Config:
        orm_mode = True
