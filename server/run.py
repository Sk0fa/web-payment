from aiohttp import web

from api.api import Api
from api.routes import get_routes


def main():
    api = Api()

    app = web.Application()
    app.on_startup.append(api.init_connection)
    app.router.add_routes(get_routes(api))

    web.run_app(app)


if __name__ == '__main__':
    main()
