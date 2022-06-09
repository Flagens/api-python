from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from rentapp import db
from . import schema
from . import services
from . import validator

router = APIRouter(

    tags=['Rooms'],
    prefix='/serviceApp'
)


@router.post('/room', status_code=status.HTTP_201_CREATED)
async def create_room(request: schema.Room, database: Session = Depends(db.get_db)):
    new_room = await services.create_new_room(request, database)
    return new_room


@router.get('/rooms', response_model=List[schema.ListRoom])
async def get_all_rooms(database: Session = Depends(db.get_db)):
    return await services.get_all_rooms(database)


@router.get('/room/{id}', response_model=schema.ListRoom)
async def room_by_id(id: int, database: Session = Depends(db.get_db)):
    return await services.get_room_by_id(id, database)


@router.delete('/room/{room_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_room_by_id(id: int, database: Session = Depends(db.get_db)):
    return await services.delete_room_by_id(id, database)
