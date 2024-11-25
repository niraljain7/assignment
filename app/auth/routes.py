from fastapi import APIRouter, HTTPException
from auth.schemas import UserCreate, Token, UserLogin
from auth.utils import create_user, authenticate_user, create_access_token


router = APIRouter()

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    create_user(user)
    access_token = create_access_token(data={"email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    user = authenticate_user(user)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"email": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
