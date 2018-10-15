import datetime
import sqlalchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date

engine = create_engine('sqlite:///sailors.db',echo = True)
Base = declarative_base()

class Sailors(Base):
    __tablename__ = 'sailors'

    sid = Column('sid',Integer, primary_key = True)
    sname = Column('sname',String(30))
    rating = Column('rating',Integer)
    age = Column('age',Integer)

    def __init__(self,sid,sname,rating,age):
        self.sid = sid
        self.sname = sname
        self.rating = rating
        self.age = age
        
Base.metadata.create_all(engine)

class Reserves(Base):
    __tablename__ = 'reserves'
    sid  = Column('sid',Integer,primary_key = True)
    bid = Column('bid',Integer,primary_key = True)
    day = Column('day',String,primary_key = True)

    def __init__(self,sid,bid,day):
        
        self.sid = sid
        self.bid = bid
        self.day = day
Base.metadata.create_all(engine)

class Boats(Base):
    __tablename__ = 'boats'
    bid = Column('bid',Integer, primary_key = True)
    bname = Column('bname',String(20))
    color = Column('color',String(10))
    length = Column('length',Integer)

    def __init__(self,bid,bname,color,length):
        self.bid = bid
        self.bname = bname
        self.color = color
        self.length = length
Base.metadata.create_all(engine)

class Payments(Base):
    __tablename__ = 'payments'
    pid = Column('pid',Integer, primary_key = True)
    sid = Column('sid',Integer)
    salary = Column('salary',Integer)
    date = Column(String)
    
    def __init__(self,pid,sid,salary,date):
        self.pid = pid
        self.sid = sid
        self.salary = salary
        self.date = date
Base.metadata.create_all(engine)


