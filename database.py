import motor.motor_asyncio
from config import MONGO_URI

def get_mongo_client():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
    return client.trading

def data_helper(data: dict) -> dict:
    _data = {}
    for key in data.keys():
        _data[key] = str(data.get(key))
    return _data

async def add_share(data: dict) -> dict:
    db = get_mongo_client()
    collection = db.get_collection("shares")
    share = await collection.insert_one(data)
    new_share = await collection.find_one({"_id": share.inserted_id})
    return data_helper(new_share)
