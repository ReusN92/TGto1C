from sqlalchemy import create_engine, Column, String, Integer, Float, MetaData,ForeignKey,Table, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *


engine = create_engine(DATABASE,echo=True)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

Data = Table('Notifications', metadata,
                        Column('id_bd', Integer,primary_key=True),
                        Column('number', String, nullable=False),
                        Column('message', String, nullable=False),
                        Column('buttons', String, nullable=False),
                        Column('id', String, nullable=False),
                        Column('file', String, nullable=True),
                        Column('send_to', String, nullable=True),
                        Column('status', String, nullable=False)
             )



metadata.create_all(engine)
