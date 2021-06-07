
async def search_stock_symbols(stock_symbol: str, session):
    async with session:
        url = f"https://api.nasdaq.com/api/quote/{stock_symbol}/info?assetclass=stocks"
        async with session.get(url) as response:
            _result = await response.json()
            return {
                'status': 200 if response.status == 200 else 404,
                'data': _result
            }
