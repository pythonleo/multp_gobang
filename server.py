import aiohttp.web as wb

routes = wb.RouteTableDef()


@routes.get('/login/{name}')
async def user_login(req):
    name = req.match_info["name"]

    if name not in req.app["users"]:
        req.app["users"][name] = {
            "name": name,
            "id": len(req.app["users"]),
            "active_battle": None
        }

    return wb.json_response(req.app["users"][name])


@routes.get('/lookup/{name}')
async def user_lookup(req):
    try:
        return wb.json_response(req.app["users"][req.match_info["name"]])
    except KeyError:
        raise wb.HTTPNotFound


app = wb.Application()
app["users"] = {}
app.add_routes(routes)
wb.run_app(app)
