from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from rentapp.db import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    beds = Column(Integer)
    price = Column(Float)


class Addons(Base):
    __tablename__ = "addons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    price = Column(Float)
