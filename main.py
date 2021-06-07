import aiohttp
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import ShareOperationModel
from nasdaq import search_stock_symbols

app = FastAPI()
session = None

@app.on_event('startup')
async def startup_event():
    global session
    session = aiohttp.ClientSession()

@app.on_event('shutdown')
async def shutdown_event():
    await session.close()

@app.get("/")
def home():
    return {"version": "1.0.0"}

@app.post("/api/v1/shares")
async def shares_operations(body: ShareOperationModel = Body(...)):
    data = jsonable_encoder(body)
    global session
    result = await search_stock_symbols(data.get('stockSymbol'), session)
    return JSONResponse(
        status_code=result.get('status'),
        content=result.get('data')
    )
