from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    DateTime,
    desc,
    func,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(Unicode, default=u'')
    created = Column(DateTime, default=func.now())
    edited = Column(DateTime, default=func.now())

    @classmethod
    def all(cls, session=None):
        """return a query with all entries, ordered by creation date reversed
        """
        if session is None:
            session = DBSession
        return session.query(cls).order_by(desc(cls.created)).all()

    @classmethod
    def by_id(cls, id, session=None):
        """return a single entry identified by id

        If no entry exists with the provided id, return None
        """
        if session is None:
            session = DBSession
        return session.query(cls).get(id)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)

    @classmethod
    def by_name(cls, name, session=None):
        if session is None:
            session = DBSession
        return DBSession.query(cls).filter(cls.name == name).first()

# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)

# Index('my_index', MyModel.name, unique=True, mysql_length=255)

