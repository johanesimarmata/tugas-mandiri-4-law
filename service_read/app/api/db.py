from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)
from databases import Database
import os

DATABASE_URI = os.getenv('DATABASE_URI') or 'postgresql://postgres:mypostgres@localhost:5432/tm4law'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

mahasiswa = Table(
    'mahasiswa',
    metadata,
    Column('npm', String(10), primary_key=True),
    Column('nama', String(250)),
)

database = Database(DATABASE_URI)