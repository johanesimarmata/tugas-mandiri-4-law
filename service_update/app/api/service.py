from fastapi import APIRouter, HTTPException
from app.api.models import Mahasiswa
from app.api.db_manager import add_mahasiswa, get_all_mahasiswa

update_service = APIRouter()
@update_service.post('/', status_code=201)
async def update_mahasiswa_service(payload: Mahasiswa):
    all_mahasiswa = await get_all_mahasiswa()
    for mahasiswa in all_mahasiswa:
        if(mahasiswa.npm == payload.npm):
            raise HTTPException(status_code=404, detail="Mahasiswa is already in database")
    await add_mahasiswa(payload)
    return {
        'status': 'OK'
    }