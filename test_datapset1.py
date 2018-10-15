import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from part2_ORM import *
from sqlalchemy.dialects.sqlite import DATE

engine = create_engine('sqlite:///sailors.db',echo = True)

#create a session
Session = sessionmaker(bind = engine)
session = Session()

#create objects
sailor = Sailors(22,"dusting",7,45.0)
session.add(sailor)

sailor = Sailors(29,"brutus",1,33.0)
session.add(sailor)

sailor = Sailors(31,"lubber",8,55.5)
session.add(sailor)

sailor = Sailors(32,"andy",8,25.5)
session.add(sailor)

sailor = Sailors(58,"rusty",10,35)
session.add(sailor)

sailor = Sailors(64,"horatio",7,16)
session.add(sailor)

sailor = Sailors(71,"zorba",10,35)
session.add(sailor)

sailor = Sailors(74,"horatio",9,25.5)
session.add(sailor)

sailor = Sailors(85,"art",3,25.5)
session.add(sailor)

sailor = Sailors(95,"bob",3,63.5)
session.add(sailor)

sailor = Sailors(23,"emilio",7,45.0)
session.add(sailor)

sailor = Sailors(24,"scruntus",1,33.0)
session.add(sailor)

sailor = Sailors(35,"figaro",8,55.5)
session.add(sailor)

sailor = Sailors(59,"stum",8,25.5)
session.add(sailor)

sailor = Sailors(60,"jit",10,35)
session.add(sailor)

sailor = Sailors(61,"ossola",7,16)
session.add(sailor)

reserve = Reserves(23,104,datetime.date("1998-10-10"))
session.add(reserve)

reserve = Reserves(24,104,"1998-10-10")
session.add(reserve)

reserve = Reserves(35,104,"1998-8-10")
session.add(reserve)

reserve = Reserves(59,105,"1998-7-10")
session.add(reserve)

reserve = Reserves(23,105,"1998-11-10")
session.add(reserve)

reserve = Reserves(35,105,"1998-11-6")
session.add(reserve)

reserve = Reserves(59,106,"1998-11-12")
session.add(reserve)

reserve = Reserves(60,106,"1998-9-5")
session.add(reserve)

reserve = Reserves(60,106,"1998-9-8")
session.add(reserve)

reserve = Reserves(88,107,"1998-9-8")
session.add(reserve)

reserve = Reserves(89,108,"1998-10-10")
session.add(reserve)

reserve = Reserves(90,109,"1998-10-10")
session.add(reserve)

reserve = Reserves(89,109,"1998-8-10")
session.add(reserve)

reserve = Reserves(60,109,"1998-7-10")
session.add(reserve)

reserve = Reserves(59,109,"1998-11-10")
session.add(reserve)

reserve = Reserves(62,110,"1998-11-6")
session.add(reserve)

reserve = Reserves(88,110,"1998-11-12")
session.add(reserve)

reserve = Reserves(88,110,"1998-9-5")
session.add(reserve)

reserve = Reserves(88,111,"1998-9-8")
session.add(reserve)

reserve = Reserves(61,112,"1998-9-8")
session.add(reserve)

reserve = Reserves(22,101,"1998-10-10")
session.add(reserve)

reserve = Reserves(22,102,"1998-10-10")
session.add(reserve)

reserve = Reserves(22,103,"1998-8-10")
session.add(reserve)

reserve = Reserves(22,104,"1998-7-10")
session.add(reserve)

reserve = Reserves(31,102,"1998-11-10")
session.add(reserve)

reserve= Reserves(31,103,"1998-11-6")
session.add(reserve)

reserve = Reserves(31,104,"1998-11-12")
session.add(reserve)

reserve = Reserves(64,101,"1998-9-5")
session.add(reserve)

reserve = Reserves(64,102,"1998-9-8")
session.add(reserve)

reserve = Reserves(74,103,"1998-9-8")
session.add(reserve)

boat = Boats(101,"Interlake","blue",45)
session.add(boat)

boat = Boats(102,"Interlake","red",45)
session.add(boat)

boat = Boats(103,"Clipper","green",40)
session.add(boat)

boat = Boats(104,"Clipper","red",40)
session.add(boat)

boat = Boats(105,"Marine","red",35)
session.add(boat)

boat = Boats(106,"Marine","green",35)
session.add(boat)

boat = Boats(107,"Marine","blue",35)
session.add(boat)

boat = Boats(108,"Driftwood","red",35)
session.add(boat)

boat = Boats(109,"Driftwood","blue",35)
session.add(boat)

boat = Boats(110,"Klapser","red",30)
session.add(boat)

boat = Boats(111,"Sooney","gren",28)
session.add(boat)

boat = Boats(112,"Sooney","red",28)
session.add(boat)

reserve = Reserves(23,104,"1998/10/10")
session.add(reserve)

#commit the record of the database
session.commit()

