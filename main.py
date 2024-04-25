from fastapi import FastAPI
from routes.api import setup_routes

app = FastAPI()
setup_routes(app)
