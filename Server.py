from aiohttp import web
import asyncio
from aiohttp_session import setup, get_session
from asyncio.base_events import _ipaddr_info
import requests

def upload_file():
    test_file = open ('my_file.txt', 'rb')
    test_url = "http://localhost:8080"
    test_response = requests.post(test_url, files = {"form_field_name": test_file})
    if test_response.ok:
        print("Upload completed successfully!")
        print(test_response.text)
    else:
        print("Something went wrong!")

async def handle(request):
    name = request.match_info.get('name', 'Virus')
    print('Connection created: ' + request.remote)
    return web.Response(text=name)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)
    upload_file()  
    


