from app.api.db import mahasiswa, database

# async def add_mahasiswa(payload: mahasiswa):
#     query = mahasiswa.insert().values(**payload.dict())
#     return await database.execute(query=query)

async def get_mahasiswa(npm):
    query = mahasiswa.select(mahasiswa.c.npm==npm)
    return await database.fetch_one(query=query)