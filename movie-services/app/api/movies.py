from fastapi import Header, APIRouter, HTTPException
from typing import List

from app.api.models import MovieIn, MovieOut
from app.api import db_manager
from app.api.services import is_cast_present

movies = APIRouter()

@movies.get('/', response_model=List[MovieOut])
async def get_movies():
  return await db_manager.get_all_movies()

@movies.get('/{id}/', response_model=MovieOut)
async def get_movie(id: int):
  movie = await db_manager.get_movie(id)
  if not movie:
    raise HTTPException(status_code=404, detail="Movie not found")
  return movie


# Add new movie with return HTTP 201
@movies.post('/', response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn):
  for cast_id in payload.casts_id:
    if not is_cast_present(cast_id):
      raise HTTPException(status_code=404, detail=f"Cast with id:{cast_id} not found")

  movie_id = await db_manager.add_movie(payload)
  response = {
    'id': movie_id,
    **payload.dict()
  }
  return response

# Update a Movie
@movies.put('/{id}/')
async def update_movie(id: int, payload: MovieIn):
  movie = await db_manager.get_movie(id)
  if not movie:
    raise HTTPException(status_code=404, detail="Movie not found")

  update_data = payload.dict(exclude_unset=True)
  movie_in_db = MovieIn(**movie)

  updated_movie = movie_in_db.copy(update=update_data)
  return await db_manager.update_movie(id, updated_movie)

# Delete a movie
@movies.delete('/{id}')
async def delete_movie(id: int):
  movie = await db_manager.get_movie(id)
  if not movie:
    raise HTTPException(status_code=404, detail="Movie not found")
  return await db_manager.delete_movie(id)
