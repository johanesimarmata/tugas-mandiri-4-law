from app.api.db import mahasiswa, database

async def get_all_mahasiswa():
    query = mahasiswa.select()
    return await database.fetch_all(query=query)

async def add_mahasiswa(payload: mahasiswa):
    query = mahasiswa.insert().values(**payload.dict())
    return await database.execute(query=query)