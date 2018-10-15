import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import alias, join, outerjoin, select, Join, Select
from sqlalchemy import text
from sqlalchemy.sql import text
from part2_ORM import *
from sqlalchemy.sql import and_, or_, not_

engine = create_engine('sqlite:///sailors.db',echo = True)
conn = engine.connect()

#create a Session
Session = sessionmaker(bind = engine)
session = Session()

#tests
stmt0 = select([Boats]) #start simple
result0 = conn.execute(stmt0).fetchall()

def test_result_stmt0():
    assert conn.execute(stmt0).fetchall()

stmt1 = select([Sailors]) 
result1 = conn.execute(stmt1).fetchall()

def test_result_stmt1():
    assert conn.execute(stmt1).fetchall()

sid, sname = column("sid"),column("sname")
stmt2 = select([sid,sname]).select_from("sailors")
result2 = conn.execute(stmt2).fetchall()

def test_result_stmt2():
    assert conn.execute(stmt2).fetchall()

stmt3 = select([func.count(distinct(Sailors.sname))])
result3 = conn.execute(stmt3).fetchall()

def test_result_stmt3():
    assert conn.execute(stmt3).fetchall()

stmt4 = text("SELECT * FROM reserves")
result4 = conn.execute(stmt4).fetchall()

def test_result_stmt4():
    assert conn.execute(stmt4).fetchall()

stmt5 = text("SELECT * FROM reserves WHERE reserves.sid=:b") #then increase difficulty
result5 = conn.execute(stmt5,b = 22).fetchall()

def test_result_stmt5():
    assert conn.execute(stmt5,b = 22).fetchall()

s = text("SELECT sailors.sid || ', ' || reserves.bid AS tests "
        "FROM sailors, reserves, boats "
        "WHERE sailors.sid = reserves.sid "
        "AND boats.color = :x"
        ) #like question 6 in part 1
s = s.columns(tests = String)
s = s.bindparams(x = 'red')
conn.execute(s).fetchall()

def test_result_s():
    assert conn.execute(s).fetchall()

t = text("SELECT sailors.sid || ', ' || sailors.sname AS reservescount "
        "FROM sailors, reserves, boats "
        "WHERE sailors.sid = reserves.sid "
        "AND reserves.bid = boats.bid "
        "AND boats.color = :z "
        "GROUP BY sailors.sid "
        "HAVING reservescount > 1"
        ) #question 3 from part 1
t = t.columns(reservescount = String)
t = t.bindparams(z = 'red')
conn.execute(t).fetchall()

def test_result_t():
    assert conn.execute(t).fetchall()

u = text("SELECT boats.bid AS reservescount "
        "FROM boats, reserves "
        "WHERE reserves.bid = boats.bid "
        "GROUP BY boats.bid "
        "HAVING reservescount > 0"
        ) #question 2 from part 1
conn.execute(u).fetchall()

def test_result_u():
    assert conn.execute(u).fetchall()

v = text("SELECT * FROM payments WHERE payments.sid = :y") #you can use the payments to see what records and transactions a sailor is associated with
conn.execute(v,y = 88).fetchall()

def test_result_v():
    assert conn.execute(v,y = 88).fetchall()

w = text("SELECT payments.pid || ', ' || payments.sid || ', ' || payments.salary AS paymentscount "
        "FROM sailors, reserves, payments, boats "
        "WHERE sailors.sid = reserves.sid "
        "AND reserves.bid = boats.bid "
        "AND sailors.sid = payments.sid "
        "GROUP BY sailors.sid "
        "HAVING paymentscount > 1"
        ) #you can use the payments to see how many times a sailor was paid 
w = w.columns(paymentscount = String)
conn.execute(w).fetchall()

def test_result_w():
    assert conn.execute(w).fetchall()
