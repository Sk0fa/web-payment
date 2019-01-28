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
        web.get('/admin', api.admin),
        web.post('/admin', api.admin_post),
        web.get('/admin/card_payments', api.card_payments),
        web.get('/admin/requested_payments', api.requested_payments),
        web.get('/logout', api.logout),
    ]
