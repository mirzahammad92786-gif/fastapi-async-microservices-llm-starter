from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
async def get_tasks():
    return {"message": "Tasks service running"}
