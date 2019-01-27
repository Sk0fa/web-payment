from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class CardPayment(Base):
    __tablename__ = 'card_payment'

    id = Column('id', Integer, primary_key=True)
    card_number = Column('card_number', String(16))
    amount = Column('amount', Integer)
    card_ttl = Column('card_ttl', Date)
    cvc = Column('cvc', String(3))
    comment = Column('comment', String(150))
    email = Column('email', String(64))
    is_safe = Column('is_safe', Boolean)


class RequestedPayment(Base):
    __tablename__ = 'requested_payment'

    id = Column('id', Integer, primary_key=True)
    tax = Column('tax', String(20))
    bic = Column('bic', String(15))
    account_number = Column('account_number', String(20))
    comment = Column('comment', String(15))
    amount = Column('amount', Integer)
    phone = Column('phone', String(15))
    email = Column('email', String(64))


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    CardPayment.__table__.create()
    RequestedPayment.__table__.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    CardPayment.__table__.drop()
    RequestedPayment.__table__.drop()
