from aiohttp import web


def auth_required(func):
    def wrapper(self, request, *args, **kwargs):
        if not request.user:
            return web.HTTPForbidden(text='Для доступа нужно авторизоваться')
        else:
            return func(self, request, *args, **kwargs)

    return wrapper
