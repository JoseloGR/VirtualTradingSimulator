from pydantic import BaseModel, conint
from enum import Enum

class TypeOperation(str, Enum):
    buy = 'buy'
    sell = 'sell'

class ShareOperationModel(BaseModel):
    stockSymbol: str
    amount: conint(gt=0)
    typeOperation: TypeOperation
