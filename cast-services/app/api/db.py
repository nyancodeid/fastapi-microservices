from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database

import os

# DATABASE_URL = 'postgresql://ryanaunur:siapgan867@localhost/movie_db'
DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

casts = Table(
  'casts',
  metadata,
  Column('id', Integer, primary_key=True),
  Column('name', String(50)),
  Column('nationality', String(20))
)

database = Database(DATABASE_URL)