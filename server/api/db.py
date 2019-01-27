import asyncpgsa
import settings
from sqlalchemy import desc, select, update
from api.models import CardPayment, RequestedPayment


class DataBase:
    def __init__(self):
        self.pool = None

    async def initialize(self):
        self.pool = await asyncpgsa.create_pool(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            min_size=5,
            max_size=30
        )

    async def create_card_payment(self, card_payment: CardPayment):
        await self._fetch_row(card_payment.__table__.insert({
            'card_number': card_payment.card_number,
            'amount': card_payment.amount,
            'card_ttl': card_payment.card_ttl,
            'cvc': card_payment.cvc,
            'comment': card_payment.comment,
            'email': card_payment.email,
            'is_safe': True,
        }))

    async def create_requested_payment(self, requested_payment: RequestedPayment):
        await self._fetch_row(requested_payment.__table__.insert({
            'tax': requested_payment.tax,
            'bic': requested_payment.bic,
            'account_number': requested_payment.account_number,
            'phone': requested_payment.phone,
            'comment': requested_payment.comment,
            'email': requested_payment.email,
            'amount': requested_payment.amount,
        }))

    async def get_card_payments(self, filter_by=None, filter_value=None, sort_by=None, sort_order=None):
        query = select([CardPayment.__table__])
        if filter_by and filter_value:
            query = query.where(getattr(CardPayment, filter_by) == filter_value)

        if sort_by:
            if not sort_order or sort_order == 'asc':
                query = query.order_by(getattr(CardPayment, sort_by))
            else:
                query = query.order_by(desc(getattr(CardPayment, sort_by)))

        return self._fetch_all(query)

    async def get_requested_payments(self, filter_by=None, filter_value=None, sort_by=None, sort_order=None):
        query = select([RequestedPayment.__table__])
        if filter_by and filter_value:
            query = query.where(getattr(RequestedPayment, filter_by) == filter_value)

        if sort_by:
            if not sort_order or sort_order == 'asc':
                query = query.order_by(getattr(RequestedPayment, sort_by))
            else:
                query = query.order_by(desc(getattr(RequestedPayment, sort_by)))

        return self._fetch_all(query)

    async def patch_card_payment(self, payment_id, is_safe):
        await self._fetch_row(
            update(CardPayment.__table__).where(CardPayment.id == payment_id).values(is_safe=is_safe)
        )

    async def _fetch_all(self, db_query, *args, **kwargs):
        async with self.pool.acquire() as connection:
            return await connection.fetch(db_query, *args, **kwargs)

    async def _fetch_row(self, query):
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(query)
