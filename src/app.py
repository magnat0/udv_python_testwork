from fastapi import FastAPI
from routing.news import router
app = FastAPI()

app.include_router(router)