import asyncio
import aiohttp
import requests
import time

urls = ["https://example.com",
        "https://python.org",
        "https://example.org"]

async def fetch(session, url):
    for _ in range(3):
        try:
            async with session.get(url) as r:
                print("Async:", url, r.status)
                return
        except:
            await asyncio.sleep(1)

async def async_crawler():
    async with aiohttp.ClientSession() as s:
        await asyncio.gather(*(fetch(s, u) for u in urls))

def sequential():
    for u in urls:
        r = requests.get(u)
        print("Sequential:", u, r.status_code)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(async_crawler())
    print("Async Time:", time.time() - start)

    start = time.time()
    sequential()
    print("Sequential Time:", time.time() - start)