from aiohttp import web

visits = 0

async def count_visits(request):
    global visits
    visits += 1
    return web.Response(text = f"Visits: {visits}")

app = web.Application()
app.router.add_get('/', count_visits)

web.run_app(app, port = 8080)