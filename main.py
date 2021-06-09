import aiohttp
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import ShareOperationModel, TypeOperation
from nasdaq import search_stock_symbols
from database import add_share

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
    if result.get('status') == 200:
        if data.get('typeOperation') == TypeOperation.buy:
            new_share = await add_share(result.get('data', {}).get('primaryData'))
            result['data'] = new_share
    return JSONResponse(
        status_code=result.get('status'),
        content=result.get('data')
    )
