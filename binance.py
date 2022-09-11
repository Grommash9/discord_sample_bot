import aiohttp


async def get_price(pair_name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api1.binance.com/api/v3/ticker/price?symbol={pair_name.upper()}') as resp:
            return await resp.json()
