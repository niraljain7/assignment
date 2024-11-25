from fastapi import FastAPI
from auth.routes import router as auth_router
from funds.routes import router as funds_router

app = FastAPI()


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(funds_router, prefix="/funds", tags=["funds"])
