import aiohttp
import asyncio
import requests


url = 'https://localhost:8080'

async def main():


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            
            r = requests.get(url, allow_redirects=True)
            open('my_file.txt', 'wb').write(r.content)
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

