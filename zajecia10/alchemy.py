from lib2to3.pytree import Base

import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import NUMERIC


class Test(Base):
    __tablename__= 'Ksiazka'
    id = Column(Integer, primary_key=True)
    name=Column(String(100))
    value=Column(NUMERIC)

engine = create_engine('sqlite:///Ksiazka.db',echo=True)

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()


for test in session.query(Test).all():
    print test.id, test.name, test.value

new_test = Test(
    id=8,
    name=u'ORM',
    value=6.8
)

session.add(new_test)
session.commit()