from fastapi import APIRouter, HTTPException
from app.api.db_manager import get_mahasiswa

read_service = APIRouter()

@read_service.get('/{npm}')
async def get_mahasiswa_service(npm: str):
    mahasiswa = await get_mahasiswa(npm)
    if not mahasiswa:
        raise HTTPException(status_code=404, detail="Mahasiswa not found")
    return {
        'status': 'OK',
        'npm': mahasiswa.npm,
        'nama': mahasiswa.nama
    }
