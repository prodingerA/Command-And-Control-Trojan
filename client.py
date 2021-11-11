from http.client import EXPECTATION_FAILED
import aiohttp
import asyncio
import urllib.request
import time
import subprocess

def download():
    nurl = 'http://localhost:8080/script2.py'
    urllib.request.urlretrieve(nurl, 'script2.py')

async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        download()
        #time.sleep(1)  
        subprocess.Popen("script2.py 1", shell=True)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())