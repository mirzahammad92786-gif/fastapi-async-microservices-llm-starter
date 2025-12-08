from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(username: str, password: str):
    return {"message": f"Logged in as {username}"}

@router.post("/signup")
async def signup(username: str, email: str):
    return {"message": f"User {username} registered successfully"}
