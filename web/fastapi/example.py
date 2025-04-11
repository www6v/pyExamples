# https://github.com/zhanymkanov/fastapi-best-practices
# https://fastapi.org.cn/reference/apirouter/
import asyncio
import time

from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, the whole process will be blocked
    
    return {"pong": True}

@router.get("/good-ping")
def good_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, but in a separate thread for the whole `good_ping` route

    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10) # non-blocking I/O operation

    return {"pong": True}


app.include_router(router)