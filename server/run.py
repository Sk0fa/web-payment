from aiohttp import web

from api.api import Api
from api.routes import get_routes


def main():
    api = Api()

    app = web.Application()
    app.on_startup.append(api.init_connection)
    app.router.add_routes(get_routes(api))
    app.router.add_static('/static/', './front/')

    web.run_app(app, port=3000)


if __name__ == '__main__':
    main()
