from sqlalchemy import (
	Column,
	Integer,
	Text,
	CHAR,
	)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm  import (
	scoped_session,
	sessionmaker,
	)

from zope.sqlalchemy  import ZopeTransactionExtension
from sqlalchemy  import create_engine

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
SQLALCHEMY_CONF_URL = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % ('root', '', '127.0.0.1', 3306, 'test')
engine = create_engine(SQLALCHEMY_CONF_URL,pool_recycle = 60)
Base.metadata.bind = engine


class MyModel(Base):
	__tablename__ = 'pyach'
	id = Column(Integer,primary_key=True)
	name = Column(CHAR(8))
	value = Column(CHAR(10))

def get_name_value():
	datas = DBSession.query(MyModel).all()
	DBSession.close()
	return datas
