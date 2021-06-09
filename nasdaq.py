
async def search_stock_symbols(stock_symbol: str, session):
    async with session:
        url = f"https://api.nasdaq.com/api/quote/{stock_symbol}/info?assetclass=stocks"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'Host': 'api.nasdaq.com',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        async with session.request('get', url, headers=headers) as response:
            response = await response.json()
            result = {
                'status': 404,
                'data': {
                    'message': 'Symbol not exists'
                }
            }
            if response.get('status', {}).get('rCode') == 200:
                result['status'] = 200
                result['data'] = response.get('data', {})
            return result
