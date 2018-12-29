import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.sql import select

engine = create_engine('sqlite:///sailors.db',echo = True)
conn = engine.connect()

metadata= MetaData()

#tables to insert into sailors database
sailors = Table('sailors',metadata,
        Column('sid',Integer,primary_key = True),
        Column('sname',String(30)),
        Column('rating',Integer),
        Column('age',Integer)
        )
reserves = Table('reserves',metadata,
        Column('sid',Integer,primary_key = True),
        Column('bid',Integer,primary_key = True),
        Column('day',String,primary_key = True)
        )
boats = Table('boats',metadata,
        Column('bid',Integer,primary_key = True),
        Column('bname',String(20)),
        Column('color',String(10)),
        Column('length',Integer)
        )
payments = Table('payments',metadata,
        Column('pid',Integer,primary_key = True),
        Column('sid',Integer),
        Column('salary',Integer),
        Column('date',String)
        )

#dictionaries to insert
conn.execute(sailors.insert(), [
    {'sid':22,'sname':'dusting','rating':7,'age':45.0},
    {'sid':29,'sname':'brutus','rating':1,'age':33.0},
    {'sid':31,'sname':'lubber','rating':8,'age':55.5},
    {'sid':32,'sname':'andy','rating':8,'age':25.5},
    {'sid':58,'sname':'rusty','rating':10,'age':35},
    {'sid':64,'sname':'horatio','rating':7,'age':16},
    {'sid':71,'sname':'zorba','rating':10,'age':35},
    {'sid':74,'sname':'horatio','rating':9,'age':25.5},
    {'sid':85,'sname':'art','rating':3,'age':25.5},
    {'sid':95,'sname':'bob','rating':3,'age':63.5},
    {'sid':23,'sname':'emilio','rating':7,'age':45.0},
    {'sid':24,'sname':'scruntus','rating':1,'age':33.0},
    {'sid':35,'sname':'figaro','rating':8,'age':55.5},
    {'sid':59,'sname':'stum','rating':8,'age':25.5},
    {'sid':60,'sname':'jit','rating':10,'age':35},
    {'sid':61,'sname':'ossola','rating':7,'age':16},
    {'sid':62,'sname':'shaun','rating':10,'age':35},
    {'sid':88,'sname':'dan','rating':9,'age':25.5},
    {'sid':89,'sname':'dye','rating':3,'age':25.5},
    {'sid':90,'sname':'vin','rating':3,'age':63.5},
    ])

conn.execute(reserves.insert(), [
    {'sid':23,'bid':104,'day':'1998/10/10'},
    {'sid':24,'bid':104,'day':'1998/10/10'},
    {'sid':35,'bid':104,'day':'1998/8/10'},
    {'sid':59,'bid':105,'day':'1998/7/10'},
    {'sid':23,'bid':105,'day':'1998/11/10'},
    {'sid':35,'bid':105,'day':'1998/11/6'},
    {'sid':59,'bid':106,'day':'1998/11/12'},
    {'sid':60,'bid':106,'day':'1998/9/5'},
    {'sid':60,'bid':106,'day':'1998/9/8'},
    {'sid':88,'bid':107,'day':'1998/9/8'},
    {'sid':89,'bid':108,'day':'1998/10/10'},
    {'sid':90,'bid':109,'day':'1998/10/10'},
    {'sid':89,'bid':109,'day':'1998/8/10'},
    {'sid':60,'bid':109,'day':'1998/7/10'},
    {'sid':59,'bid':109,'day':'1998/11/10'},
    {'sid':62,'bid':110,'day':'1998/11/6'},
    {'sid':88,'bid':110,'day':'1998/11/12'},
    {'sid':88,'bid':110,'day':'1998/9/5'},
    {'sid':88,'bid':111,'day':'1998/9/8'},
    {'sid':61,'bid':112,'day':'1998/9/8'},
    {'sid':22,'bid':101,'day':'1998/10/10'},
    {'sid':22,'bid':102,'day':'1998/10/10'},
    {'sid':22,'bid':103,'day':'1998/8/10'},
    {'sid':22,'bid':104,'day':'1998/7/10'},
    {'sid':31,'bid':102,'day':'1998/11/10'},
    {'sid':31,'bid':103,'day':'1998/11/6'},
    {'sid':31,'bid':104,'day':'1998/11/12'},
    {'sid':64,'bid':101,'day':'1998/9/5'},
    {'sid':64,'bid':102,'day':'1998/9/8'},
    {'sid':74,'bid':103,'day':'1998/9/8'},
    ])

conn.execute(boats.insert(), [
    {'bid':101,'bname':'Interlake','color':'blue','length':45},
    {'bid':102,'bname':'Interlake','color':'red','length':45},
    {'bid':103,'bname':'Clipper','color':'green','length':40},
    {'bid':104,'bname':'Clipper','color':'red','length':40},
    {'bid':105,'bname':'Marine','color':'red','length':35},
    {'bid':106,'bname':'Marine','color':'green','length':35},
    {'bid':107,'bname':'Marine','color':'blue','length':35},
    {'bid':108,'bname':'Driftwood','color':'red','length':35},
    {'bid':109,'bname':'Driftwood','color':'blue','length':35},
    {'bid':110,'bname':'Klapser','color':'red','length':30},
    {'bid':111,'bname':'Sooney','color':'gren','length':28},
    {'bid':112,'bname':'Sooney','color':'red','length':28},
    ])

conn.execute(payments.insert(), [
    {'pid':1,'sid':22,'salary':1000,'date':'1998/8/10'},
    {'pid':2,'sid':22,'salary':1000,'date':'1998/9/10'},
    {'pid':3,'sid':22,'salary':2000,'date':'1998/11/10'},
    {'pid':4,'sid':23,'salary':1000,'date':'1998/11/10'},
    {'pid':5,'sid':23,'salary':1000,'date':'1998/12/10'},
    {'pid':6,'sid':24,'salary':1000,'date':'1998/11/10'},
    {'pid':7,'sid':31,'salary':3000,'date':'1998/12/6'},
    {'pid':8,'sid':35,'salary':1000,'date':'1998/12/6'},
    {'pid':9,'sid':35,'salary':1000,'date':'1998/9/10'},
    {'pid':10,'sid':59,'salary':1000,'date':'1998/8/10'},
    {'pid':11,'sid':59,'salary':1000,'date':'1998/12/10'},
    {'pid':12,'sid':60,'salary':2000,'date':'1998/10/6'},
    {'pid':13,'sid':60,'salary':1000,'date':'1998/8/10'},
    {'pid':14,'sid':61,'salary':1000,'date':'1998/10/8'},
    {'pid':15,'sid':62,'salary':1000,'date':'1998/12/6'},
    {'pid':16,'sid':64,'salary':2000,'date':'1998/10/5'},
    {'pid':17,'sid':74,'salary':1000,'date':'1998/10/8'},
    {'pid':18,'sid':88,'salary':3000,'date':'1998/10/5'},
    {'pid':19,'sid':88,'salary':1000,'date':'1998/12/12'},
    {'pid':20,'sid':89,'salary':1000,'date':'1998/9/10'},
    {'pid':21,'sid':89,'salary':1000,'date':'1998/11/10'},
    {'pid':22,'sid':90,'salary':1000,'date':'1998/11/10'},
])
