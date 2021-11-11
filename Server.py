from aiohttp import web

async def handle(request):
    name = request.match_info.get('name')
    print('Connection created: ' + request.remote)
    try:
        file = open(name, 'r')
        content = file.read()
        file.close()
        return web.Response(text=content)
    except FileNotFoundError:
        return 'Sorry file not here lol'

app = web.Application()
app.add_routes([web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app) 
    


