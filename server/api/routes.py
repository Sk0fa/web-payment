from aiohttp import web


def get_routes(api):
    return [
        web.post('/api/card_payment', api.card_payment_post),
        web.post('/api/requested_payment', api.requested_payment_post),
        web.get('/api/card_payment', api.card_payment_get),
        web.get('/api/requested_payment', api.requested_payment_get),
        web.patch('/api/card_payment', api.card_payment_patch),
        web.post('/api/internet_bank_payment', api.internet_bank_payment),
        web.get('/payment/{customer}', api.payment_customer),
    ]
