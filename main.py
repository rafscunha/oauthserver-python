from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from tortoise.contrib.fastapi import  register_tortoise
from tortoise import Tortoise
from connection.mariadb import TORTOISE_CONFIG, TORTOISE_MODELS
from routes import route_auth, route_user

app = FastAPI()

app.include_router(route_user.router)
app.include_router(route_auth.router)

Tortoise.init_models(TORTOISE_MODELS,"models")
register_tortoise(
    app,
    config=TORTOISE_CONFIG,
    add_exception_handlers=True
)
