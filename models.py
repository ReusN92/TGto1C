from sqlalchemy import create_engine, Column, String, Integer, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config import DATABASE


engine = create_engine(DATABASE,echo=True)
Session = sessionmaker(bind=engine)
base = declarative_base(engine)
session = Session()

class dbm:
    __slots__ = ['session']

    def __enter__(self):
        self.session = session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        self.session.close()



class Notifications(base):
    __tablename__ = 'Notifications'

    id_bd = Column(Integer,primary_key=True)
    number = Column(Integer, nullable=False)
    message = Column(String,nullable=False)
    id = Column(String,nullable=False)
    file = Column(String, nullable=True)
    send_to = Column(String,nullable=True)



    def __repr__(self):
        return "'%s','%s','%s','%s','%s','%s'" % \
               (self.id_bd,self.number,self.message, self.id,self.file,self.send_to)