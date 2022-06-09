from typing import List

from fastapi import HTTPException, status

from . import models


async def create_new_room(request, database) -> models.Rooms:
    new_room = models.Rooms(name=request.name, beds=request.beds, price=request.price)
    database.add(new_room)
    database.commit()
    database.refresh(new_room)
    return new_room


async def get_all_rooms(database) -> List[models.Rooms]:
    rooms = database.query(models.Rooms).all()
    return rooms


async def get_room_by_id(id,database)->models.Rooms:
    room=database.query(models.Rooms).get(id)
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data Not Found!")
    return room


async def delete_room_by_id(id,database):
    database.query(models.Rooms).filter(models.Rooms.id == id).delete()
    database.commit()
