import datetime
import sqlalchemy
import argparse
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import text
from sqlalchemy import func

engine = create_engine('sqlite:///cucc.db',echo = True)
Base = declarative_base()

class Workers(Base):
    __tablename__ = 'workers'

    wid = Column('wid',Integer,primary_key = True)
    wname = Column('wname',String(30))

    def __init__(self,wid,wname):
        self.wid = wid
        self.wname = wname

    def __repr__(self):
        return "<Worker (id = '%d', name = %s)>" % (self.wid,self.wname)

Base.metadata.create_all(engine)

class Supervisors(Base):
    __tablename__ = 'supervisors'

    sid = Column('sid',Integer,primary_key = True)
    sname = Column('sname',String(30))
    sdateapproval = Column('sdateapproval',String(30))
    sdatedecline = Column('sdatedecline',String(30))
    sdatesubmission = Column('sdatesubmission',String(30))

    def __init__(self,sid,sname,sdateapproval,sdatedecline,sdatesubmission):
        self.sid = sid
        self.sname = sname
        self.sdateapproval = sdateapproval     
        self.sdatedecline = sdatedecline
        self.sdatesubmission = sdatesubmission

    def __repr__(self):
        return "<Supervisor(sid = '%s',sname = '%s',sdateapproval = '%s',sdatedecline = '%s',sdatesubmission = '%s')>" % (self.sid,self.sname,self.sdateapproval,self.sdatedecline,self.sdatesubmission)

Base.metadata.create_all(engine)

class Worked(Base):
    __tablename__ = 'worked'

    wkd_no = Column('wkd_no',Integer,primary_key = True)
    wkd_id = Column('wkd_id',Integer)
    wkd_date = Column('wkd_date',String(30))
    wkd_rate = Column('wkd_rate',Integer)
    wkd_hours = Column('wkd_hours',Float)
    
    def __init__(self,wkd_no,wkd_id,wkd_date,wkd_rate,wkd_hours):
        self.wkd_no = wkd_no
        self.wkd_id = wkd_id
        self.wkd_date = wkd_date
        self.wkd_rate = wkd_rate
        self.wkd_hours = wkd_hours

    def __repr__(self):
        return "<Worked (wkd_no = '%s',wkd_id = '%s',wkd_date = '%s',wkd_rate = '%s',wkd_hours = '%s')>" % (self.wkd_no,self.wkd_id,self.wkd_date,self.wkd_rate,self.wkd_hours)

Base.metadata.create_all(engine)

class Workeds(Base):
    __tablename__ = 'workeds'

    wkds_no = Column('wkds_no',Integer,primary_key = True)
    wkds_id = Column('wkds_id',Integer)
    wkds_date = Column('wkds_date',String(30))
    wkds_rate = Column('wkds_rate',Integer)
    wkds_hours = Column('wkds_hours',Float)
    
    def __init__(self,wkds_no,wkds_id,wkds_date,wkds_rate,wkds_hours):
        self.wkds_no = wkds_no
        self.wkds_id = wkds_id
        self.wkds_date = wkds_date
        self.wkds_rate = wkds_rate
        self.wkds_hours = wkds_hours

    def __repr__(self):
        return "<Workeds (wkds_no = '%s',wkds_id = '%s',wkds_date = '%s',wkds_rate = '%s',wkds_hours = '%s')>" %(self.wkds_no,self.wkds_id,self.wkds_date,self.wkds_rate,self.wkds_hours)
    
Base.metadata.create_all(engine)

class Payroll(Base):
    __tablename__ = 'payroll'

    pno = Column('pno',Integer,primary_key = True)
    pdates = Column('pdates',String(30))
    pid = Column('pid',Integer)
    pgross = Column('pgross',Float)

    def __init__(self,pno,pdates,pid,pgross):
        self.pno = pno
        self.pdates = pdates
        self.pid = pid
        self.pgross = pgross

    def __repr__(self):
        return "<Payroll (pno = '%s', pdates = '%s', pid = '%s', pgross = '%s')>" % (self.pno,self.pdates,self.pid,self.pgross)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
Session.configure(bind = engine)
session = Session()
session.add_all([
    Workers(wid = 1,wname = 'Ehit Agarwal'),
    Workers(wid = 2,wname = 'Mahir Alam'),
    Workers(wid = 3,wname = 'Isaac Alboucai'),
    Workers(wid = 4,wname = 'Aziza Almanakly'),
    Workers(wid = 5,wname = 'Gregiore Caubel'),
    Workers(wid = 6,wname = 'Hanoch Goldfarb'),
    Workers(wid = 7,wname = 'Yilang Hao'),
    Workers(wid = 8,wname = 'Will Henderson'),
    Workers(wid = 9,wname = 'Zhekai Jin'),
    Workers(wid = 10,wname = 'Dongkyu Kim'),
    Workers(wid = 11,wname = 'Junbum Kim'),
    Workers(wid = 12,wname = 'Thomas Koch'),
    Workers(wid = 13,wname = 'Wai Yan Nyein'),
    Workers(wid = 14,wname = 'Donghyun Park'),
    Workers(wid = 15,wname = 'Heuiyoung Park'),
    Workers(wid = 16,wname = 'Timil Patel'),
    Workers(wid = 17,wname = 'Alinur Rahim'),
    Workers(wid = 18,wname = 'Tianshu Ren'),
    Workers(wid = 19,wname = 'Giovanni Sanchez'),
    Workers(wid = 20,wname = 'Netanel Saso'),
    Workers(wid = 22,wname = 'Nithi Subbaian'),
    Workers(wid = 23,wname = 'Zhichun Sun'),
    Workers(wid = 24,wname = 'Austin Wong'),
    Workers(wid = 25,wname = 'Jiachen Xu'),
    Workers(wid = 26,wname = 'Wentao Zhang'),
    Workers(wid = 27,wname = 'Liao Hu'),
    Workers(wid = 28,wname = 'Sirui Yang'),
    Workers(wid = 29,wname = 'Joelsy Fernandez'),
    Workers(wid = 30,wname = 'Carena Toy'),
    Workers(wid = 31,wname = 'Aidan Smolar'),
    Workers(wid = 32,wname = 'Evan Bubniak'),
    Workers(wid = 33,wname = 'Kevin Jiang'),
    Workers(wid = 34,wname = 'Syed Naqui'),
    Supervisors(sid = 100,sname = 'Shailesh Patro',sdateapproval = '11/20/2018',sdatedecline = 'NULL',sdatesubmission = '11/20/2018'),
    Supervisors(sid = 200,sname = 'Yingzhi Hao',sdateapproval = '11/19/2018',sdatedecline = 'NULL',sdatesubmission = 'NULL'),
    Supervisors(sid = 300,sname = 'Min Joon So',sdateapproval = 'NULL',sdatedecline = 'NULL',sdatesubmission = 'NULL'),
    Supervisors(sid = 400,sname = 'Sam Cheng',sdateapproval = 'NULL',sdatedecline = 'NULL',sdatesubmission = 'NULL'),
    Supervisors(sid = 500,sname = 'Alex Lee',sdateapproval = 'NULL',sdatedecline = 'NULL',sdatesubmission = 'NULL'),
    Supervisors(sid = 600,sname = 'John Nguyen',sdateapproval = 'NULL',sdatedecline = 'NULL',sdatesubmission = 'NULL'),
    Supervisors(sid = 700,sname = 'Arthur Watkins',sdateapproval = 'NULL',sdatedecline = 'NULL',sdatesubmission = 'NULL'),
    Supervisors(sid = 800,sname = 'Jasmine Tang',sdateapproval = 'NULL',sdatedecline = 'NULL',sdatesubmission = 'NULL'),
    Worked(wkd_no = 1,wkd_id = 1,wkd_date = '11/03/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 2,wkd_id = 10,wkd_date = '11/03/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 3,wkd_id = 10,wkd_date = '11/04/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 4,wkd_id = 32,wkd_date = '11/04/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 5,wkd_id = 31,wkd_date = '11/04/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 6,wkd_id = 7,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 7,wkd_id = 11,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 8,wkd_id = 17,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 9,wkd_id = 23,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 10,wkd_id = 26,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 11,wkd_id = 27,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 12,wkd_id = 33,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 13,wkd_id = 34,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 14,wkd_id = 31,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 15,wkd_id = 29,wkd_date = '11/05/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 16,wkd_id = 7,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 17,wkd_id = 10,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 18,wkd_id = 11,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 19,wkd_id = 23,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 20,wkd_id = 26,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 21,wkd_id = 34,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 22,wkd_id = 30,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 23,wkd_id = 31,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 24,wkd_id = 32,wkd_date = '11/06/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 25,wkd_id = 6,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 26,wkd_id = 10,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 27,wkd_id = 13,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 28,wkd_id = 23,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 29,wkd_id = 24,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 7),
    Worked(wkd_no = 30,wkd_id = 27,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 31,wkd_id = 29,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 32,wkd_id = 31,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 33,wkd_id = 30,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 5),
    Worked(wkd_no = 34,wkd_id = 32,wkd_date = '11/07/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 35,wkd_id = 6,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 36,wkd_id = 7,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 37,wkd_id = 10,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 38,wkd_id = 13,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 39,wkd_id = 24,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 40,wkd_id = 27,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 41,wkd_id = 32,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 7),
    Worked(wkd_no = 42,wkd_id = 30,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 43,wkd_id = 34,wkd_date = '11/08/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 44,wkd_id = 13,wkd_date = '11/09/2018',wkd_rate = 13,wkd_hours = 3), 
    Worked(wkd_no = 45,wkd_id = 16,wkd_date = '11/09/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 46,wkd_id = 17,wkd_date = '11/09/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 47,wkd_id = 24,wkd_date = '11/09/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 48,wkd_id = 32,wkd_date = '11/09/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 49,wkd_id = 30,wkd_date = '11/09/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 50,wkd_id = 10,wkd_date = '11/10/2018',wkd_rate = 13,wkd_hours = 8),
    Worked(wkd_no = 51,wkd_id = 1,wkd_date = '11/11/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 52,wkd_id = 10,wkd_date = '11/11/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 53,wkd_id = 15,wkd_date = '11/11/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 54,wkd_id = 7,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 55,wkd_id = 11,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 56,wkd_id = 13,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 57,wkd_id = 18,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 58,wkd_id = 23,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 59,wkd_id = 24,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 60,wkd_id = 26,wkd_date= '11/12/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 61,wkd_id = 27,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 62,wkd_id = 33,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 63,wkd_id = 34,wkd_date = '11/12/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 64,wkd_id = 29,wkd_date= '11/12/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 65,wkd_id = 7,wkd_date = '11/13/2018',wkd_rate = 13,wkd_hours = 5),
    Worked(wkd_no = 66,wkd_id = 10,wkd_date= '11/13/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 67,wkd_id = 11,wkd_date= '11/13/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 68,wkd_id = 23,wkd_date = '11/13/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 69,wkd_id = 26,wkd_date = '11/13/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 70,wkd_id = 33,wkd_date = '11/13/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 71,wkd_id = 30,wkd_date= '11/13/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 72,wkd_id = 31,wkd_date = '11/13/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 73,wkd_id = 32,wkd_date = '11/13/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 74,wkd_id = 3,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 75,wkd_id = 10,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 6),
    Worked(wkd_no = 76,wkd_id = 17,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 77,wkd_id = 6,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 78,wkd_id = 13,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 79,wkd_id = 24,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 80,wkd_id = 23,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 81,wkd_id = 31,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 4),
    Worked(wkd_no = 82,wkd_id = 30,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 5),
    Worked(wkd_no = 83,wkd_id = 32,wkd_date = '11/14/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 84,wkd_id = 1,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 85,wkd_id = 6,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 5),
    Worked(wkd_no = 86,wkd_id = 7,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 87,wkd_id = 13,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 88,wkd_id = 17,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 3),
    Worked(wkd_no = 89,wkd_id = 30,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 5),
    Worked(wkd_no = 90,wkd_id = 29,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 2),
    Worked(wkd_no = 91,wkd_id = 29,wkd_date = '11/16/2018',wkd_rate = 13,wkd_hours = 3),
    Workeds(wkds_no = 1,wkds_id = 600,wkds_date = '11/03/2018',wkds_rate = 15,wkds_hours = 4),
    Workeds(wkds_no = 2,wkds_id = 500,wkds_date = '11/04/2018',wkds_rate = 15,wkds_hours = 6),
    Workeds(wkds_no = 3,wkds_id = 200,wkds_date = '11/05/2018',wkds_rate = 15,wkds_hours = 4),
    Workeds(wkds_no = 4,wkds_id = 300,wkds_date = '11/05/2018',wkds_rate = 15,wkds_hours = 2),
    Workeds(wkds_no = 5,wkds_id = 600,wkds_date = '11/05/2018',wkds_rate = 15,wkds_hours = 2),
    Workeds(wkds_no = 6,wkds_id = 200,wkds_date = '11/06/2018',wkds_rate = 15,wkds_hours = 2),
    Workeds(wkds_no = 7,wkds_id = 500,wkds_date = '11/06/2018',wkds_rate = 15,wkds_hours = 4),
    Workeds(wkds_no = 8,wkds_id = 600,wkds_date = '11/06/2018',wkds_rate = 15,wkds_hours = 5),
    Workeds(wkds_no = 9,wkds_id = 200,wkds_date = '11/07/2018',wkds_rate = 15,wkds_hours = 3),
    Workeds(wkds_no = 10,wkds_id = 300,wkds_date = '11/07/2018',wkds_rate = 15,wkds_hours = 2),
    Workeds(wkds_no = 11,wkds_id = 600,wkds_date = '11/07/2018',wkds_rate = 15,wkds_hours = 5),
    Workeds(wkds_no = 12,wkds_id = 200,wkds_date = '11/12/2018',wkds_rate = 15,wkds_hours = 4),
    Workeds(wkds_no = 13,wkds_id = 300,wkds_date = '11/12/2018',wkds_rate = 15,wkds_hours = 2),
    Workeds(wkds_no = 14,wkds_id = 600,wkds_date = '11/12/2018',wkds_rate = 15,wkds_hours = 3),
    Workeds(wkds_no = 15,wkds_id = 700,wkds_date = '11/12/2018',wkds_rate = 15,wkds_hours = 4),
    Payroll(pno = 1,pdates = '11/03/2018-11/16/2018',pid = 1,pgross = 78),
    Payroll(pno = 2,pdates = '11/03/2018-11/16/2018',pid = 2,pgross = 0),
    Payroll(pno = 3,pdates = '11/03/2018-11/16/2018',pid = 3,pgross = 26),
    Payroll(pno = 4,pdates = '11/03/2018-11/16/2018',pid = 4,pgross = 0),
    Payroll(pno = 5,pdates = '11/03/2018-11/16/2018',pid = 5,pgross = 0),
    Payroll(pno = 6,pdates = '11/03/2018-11/16/2018',pid = 6,pgross = 143),
    Payroll(pno = 7,pdates = '11/03/2018-11/16/2018',pid = 7,pgross = 338),
    Payroll(pno = 8,pdates = '11/03/2018-11/16/2018',pid = 8,pgross = 0),
    Payroll(pno = 9,pdates = '11/03/2018-11/16/2018',pid = 9,pgross = 0),
    Payroll(pno = 10,pdates = '11/03/2018-11/16/2018',pid = 10,pgross = 520),
    Payroll(pno = 11,pdates = '11/03/2018-11/16/2018',pid = 11,pgross = 156),
    Payroll(pno = 12,pdates = '11/03/2018-11/16/2018',pid = 12,pgross = 0),
    Payroll(pno = 13,pdates = '11/03/2018-11/16/2018',pid = 13,pgross = 195),
    Payroll(pno = 14,pdates = '11/03/2018-11/16/2018',pid = 14,pgross = 0),
    Payroll(pno = 15,pdates = '11/03/2018-11/16/2018',pid = 15,pgross = 52),
    Payroll(pno = 16,pdates = '11/03/2018-11/16/2018',pid = 16,pgross = 52),
    Payroll(pno = 17,pdates = '11/03/2018-11/16/2018',pid = 17,pgross = 156),
    Payroll(pno = 18,pdates = '11/03/2018-11/16/2018',pid = 18,pgross = 26),
    Payroll(pno = 19,pdates = '11/03/2018-11/16/2018',pid = 19,pgross = 0),
    Payroll(pno = 20,pdates = '11/03/2018-11/16/2018',pid = 20,pgross = 0),
    Payroll(pno = 21,pdates = '11/03/2018-11/16/2018',pid = 21,pgross = 0),
    Payroll(pno = 22,pdates = '11/03/2018-11/16/2018',pid = 22,pgross = 0),
    Payroll(pno = 23,pdates = '11/03/2018-11/16/2018',pid = 23,pgross = 182),
    Payroll(pno = 24,pdates = '11/03/2018-11/16/2018',pid = 24,pgross = 208),
    Payroll(pno = 25,pdates = '11/03/2018-11/16/2018',pid = 25,pgross = 0),
    Payroll(pno = 26,pdates = '11/03/2018-11/16/2018',pid = 26,pgross = 130),
    Payroll(pno = 27,pdates = '11/03/2018-11/16/2018',pid = 27,pgross = 156),
    Payroll(pno = 28,pdates = '11/03/2018-11/16/2018',pid = 28,pgross = 0),
    Payroll(pno = 29,pdates = '11/03/2018-11/16/2018',pid = 29,pgross = 182),
    Payroll(pno = 30,pdates = '11/03/2018-11/16/2018',pid = 30,pgross = 351),
    Payroll(pno = 31,pdates = '11/03/2018-11/16/2018',pid = 31,pgross = 247),
    Payroll(pno = 32,pdates = '11/03/2018-11/16/2018',pid = 32,pgross = 455),
    Payroll(pno = 33,pdates = '11/03/2018-11/16/2018',pid = 33,pgross = 91),
    Payroll(pno = 34,pdates = '11/03/2018-11/16/2018',pid = 34,pgross = 104),
    Payroll(pno = 35,pdates = '11/03/2018-11/16/2018',pid = 100,pgross = 0),
    Payroll(pno = 36,pdates = '11/03/2018-11/16/2018',pid = 200,pgross = 195),
    Payroll(pno = 37,pdates = '11/03/2018-11/16/2018',pid = 300,pgross = 90),
    Payroll(pno = 38,pdates = '11/03/2018-11/16/2018',pid = 400,pgross = 0),
    Payroll(pno = 39,pdates = '11/03/2018-11/16/2018',pid = 500,pgross = 150),
    Payroll(pno = 40,pdates = '11/03/2018-11/16/2018',pid = 600,pgross = 285),
    Payroll(pno = 41,pdates = '11/03/2018-11/16/2018',pid = 700,pgross = 60)
    ])

session.commit()

#for instance in session.query(Workers).order_by(Workers.wname):
#    print (instance.wid,instance.wname)

#for sid,sname in session.query(Supervisors.sid,Supervisors.sname):
#    print(sid,sname)

#for row in session.query(Worked,Worked.wkd_no,Worked.wkd_id,Worked.wkd_date,Worked.wkd_hours).all():    
#    print(row.Worked,row.wkd_no,row.wkd_id,row.wkd_date,row.wkd_hours)

#for row in session.query(Workeds.wkds_id.label('supervisor_id_label')).all():
#    print (row.supervisor_id_label)

#for u in session.query(Worked).order_by(Worked.wkd_id):
#    print (u)

#for sname, in session.query(Supervisors.sname).\
#        filter_by(sname = 'Yingzhi Hao'):
#            print(sname)

#for worker in session.query(Worked).\
#        filter(Worked.wkd_date == '11/08/2018').\
#        filter(Worked.wkd_hours <= 2):
#        print (worker)

#session.query(Workers).filter(Workers.wid).count()
#session.query(func.count(Workers.wname),Workers.wname).group_by(Workers.wname).all()
#session.query(func.count(Workers.wid)).scalar()

#for w, wkd in session.query(Workers,Worked).\
#        filter(Workers.wid == Worked.wkd_id).\
#        order_by(Worked.wkd_id):
#            print (w)
#            print (wkd)

#q = (session.query(Workers,Worked).filter(Workers.wid == Worked.wkd_id).all())
#r = (session.query(Supervisors,Workeds).filter(Supervisors.sid == Workeds.wkds_id).all())

#parser = argparse.ArgumentParser(description = 'Tool for using cucc database')
#parser.add_argument('integers',metavar = 'N',type = int,nargs = '+',help = 'integer list')
#parser.add_argument('--sum',action = 'store_const',const = sum,default = max,help = 'sum the integers(default: find the max)')
#parser.add_argument('--supervisor',nargs = 1,type = int, choices = range(100,900),help = 'enter in student id')
#parser.add_argument('--view',nargs = 1,r,help = 'view time schedule')
#args = parser.parse_args()
#print()

import sys

def main():
    script = sys.argv[0]
    user = sys.argv[1]
    no = sys.argv[2]
    action = sys.argv[3]
    args = sys.argv[4:]
    assert user in ['--operator','--supervisor'], \
            'User is not one of --operator or --supervisor: ' + user
    assert action in ['--clockin','--view'], \
            'Action is not one of --clockin or --view: ' + action
    if user == '--supervisor':
        assert no in ['100','200','300','400','500','600','700','800'], \
                'Error: invalid supervisor ID number. ' + no
        process(user,action)
    else:
        assert no in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34'], \
                'Error: invalid operator ID number. ' + no
        protocol(user,action)

def process(user,action):
    if action == '--clockin':
        values = session.add(Workeds(wkds_no = sys.argv[4],wkds_id = sys.argv[5],wkds_date = sys.argv[6],wkds_rate = sys.argv[7],wkds_hours = sys.argv[8]))
        print("Success")
    elif action == '--view':
        values = (session.query(Payroll).filter(Payroll.pid == sys.argv[4]).all())
        print(values)

def protocol(user,action):
    if action == '--clockin':
        values = session.add(Worked(wkd_no = sys.argv[4],wkd_id = sys.argv[5],wkd_date = sys.argv[6],wkd_rate = sys.argv[7],wkd_hours = sys.argv[8]))
        print("Success")
    elif action == '--view':
        print("Error: you do not have permission to do this.")

main()
