from fastapi import FastAPI
from fastapi import Request
from fastapi import Query
from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from fastapi.responses import PlainTextResponse
from client import CLIENT
from InputData import LoginSession
from SessionCipher import Cipher

app = FastAPI()

async def authorize(request: Request):
    Key = request.query_params.get("key", "")
    try:
        Data = Cipher(Data = LoginSession, key = Key).decrypt()
        return Data
    except:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "invalid Key"
        )

@app.get("/")
async def index(Authorize: authorize = Depends(), limit:int = Query(gt=14, lt=201, default=100)):
    Configs = await CLIENT(
        Data = eval(Authorize)
    ).GetConfigs(LimitMsg=limit)
    return PlainTextResponse(
        content = Configs
    )
    