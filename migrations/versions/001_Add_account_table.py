from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    login = Column('login', String(40))
    password = Column('password', String(64))


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    User.__table__.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    User.__table__.drop()
