from fastapi import FastAPI
from routes.user import user
import uvicorn

app = FastAPI()
app.include_router(user)

# @app.get("/")
# async def root():
#     return {"Hej"}

