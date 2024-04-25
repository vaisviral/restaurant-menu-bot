from fastapi import APIRouter, FastAPI
from fastapi.responses import PlainTextResponse

router = APIRouter()


def setup_routes(app: FastAPI):
    app.include_router(router, prefix="", tags=["api"])


@router.get("/")
async def read_root():
    return PlainTextResponse(status_code=200, content="Скоро будет работать")


@router.get("/status", description="Get API status.")
def get_status():
    return PlainTextResponse(status_code=200, content="OK")
