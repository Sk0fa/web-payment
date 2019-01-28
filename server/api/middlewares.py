from datetime import datetime

from aiohttp.web import middleware
from aiohttp.web_request import Request

from api.common import SESSION_IDS_TO_USER


def get_middlewares():
    return [
        auth_middleware,
        logging_middleware,
    ]


@middleware
async def auth_middleware(request, handler):
    cookies = request.cookies
    sid = cookies.get('sid')

    if sid and SESSION_IDS_TO_USER.get(sid):
        setattr(request, 'user', SESSION_IDS_TO_USER[sid])
    else:
        setattr(request, 'user', None)

    return await handler(request)


@middleware
async def logging_middleware(request: Request, handler):
    print(
        f'{datetime.now().strftime("%H:%M:%S")} {request.method} '
        f'{request.raw_path} {request.query_string} {request.host}'
    )

    return await handler(request)
