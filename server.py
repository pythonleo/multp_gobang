import aiohttp.web as wb

routes = wb.RouteTableDef()


@routes.get('/')
async def hello_world(_):
    return wb.json_response({"data": "Hello world!"})


app = wb.Application()
app.add_routes(routes)
wb.run_app(app)
