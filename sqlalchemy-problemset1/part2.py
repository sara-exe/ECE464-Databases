import sqlite3

conn = sqlite3.connect("C:\\~\\Documents\\sqlalchemy-problemset1\\sailors.db")

c = conn.cursor()
c.execute('''DROP TABLE sailors''') #it wouldn't compile for me as I debugged unless I did dropped the tables because it kept giving me that the tables already exists error
c.execute('''DROP TABLE reserves''')
c.execute('''DROP TABLE boats''')

c.execute('''
        CREATE TABLE sailors
        (sid int PRIMARY KEY, sname varchar(30), rating int, age int)
        ''')
c.execute('''
        CREATE TABLE reserves
        (sid int, bid int, day date, PRIMARY KEY (sid, bid, day))
        ''')
c.execute('''
        CREATE TABLE boats
        (bid int PRIMARY KEY, bname char (20), color char (20), length int)
        ''')

c.execute('''
        INSERT INTO sailors VALUES (22,'dusting',7,45.0)
       ''')
c.execute('''
        INSERT INTO sailors VALUES (29,'brutus',1,33.0)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (31,'lubber',8,55.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (32,'andy',8,25.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (58,'rusty',10,35)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (64,'horatio',7,16)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (71,'zorba',10,35)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (74,'horatio',9,25.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (85,'art',3,25.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (95,'bob',3,63.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (23,'emilio',7,45.0)
        ''')
c.execute('''       
        INSERT INTO sailors VALUES (24,'scruntus',1,33.0)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (35,'figaro',8,55.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (59,'stum',8,25.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (60,'jit',10,35)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (61,'ossola',7,16)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (62,'shaun',10,35)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (88,'dan',9,25.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (89,'dye',3,25.5)
        ''')
c.execute('''
        INSERT INTO sailors VALUES (90,'vin',3,65.5)
        ''')

c.execute('''
        INSERT INTO reserves VALUES (23,104,'1998/10/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (24,104,'1998/10/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (35,104,'1998/8/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (59,105,'1998/7/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (23, 105,'1998/11/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (35,105,'1998/11/6')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (59,106,'1998/11/12')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (60,106,'1998/9/5')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (60,106,'1998/9/8')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (88,107,'1998/9/8')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (89,108,'1998/10/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (90,109,'1998/10/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (89,109,'1998/8/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (60,109,'1998/7/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (59,109,'1998/11/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (62,110,'1998/11/6')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (88,110,'1998/11/12')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (88,110,'1998/9/5')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (88,111,'1998/9/8')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (61,112,'1998/9/8')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (22,101,'1998/10/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (22,102,'1998/10/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (22,103,'1998/8/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (22,104,'1998/7/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (31,102,'1998/11/10')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (31,103,'1998/11/6')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (31,104,'1998/11/12')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (64,101,'1998/9/5')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (64,102,'1998/9/8')
        ''')
c.execute('''
        INSERT INTO reserves VALUES (74,103,'1998/9/8')
        ''')

c.execute('''
        INSERT INTO boats VALUES (101,'Interlake','blue',45)
        ''')
c.execute('''
        INSERT INTO boats VALUES (102,'Interlake','red',45)
        ''')
c.execute('''
        INSERT INTO boats VALUES (103,'Clipper','green',40)
        ''')
c.execute('''
        INSERT INTO boats VALUES (104,'Clipper','red',40)
        ''')
c.execute('''
        INSERT INTO boats VALUES (105,'Marine','red',35)
        ''')
c.execute('''
        INSERT INTO boats VALUES (106,'Marine','green',35)
        ''')
c.execute('''
        INSERT INTO boats VALUES (107,'Marine','blue',35)
        ''')
c.execute('''
        INSERT INTO boats VALUES (108,'Driftwoord','red',35)
        ''')
c.execute('''
        INSERT INTO boats VALUES (109,'Driftwood','blue',35)
        ''')
c.execute('''
        INSERT INTO boats VALUES (110,'Klapser','red',30)
        ''')
c.execute('''
        INSERT INTO boats VALUES (111,'Sooney','gren',28)
        ''')
c.execute('''
        INSERT INTO boats VALUES (112,'Sooney','red',28)
        ''')

conn.commit()
conn.close()

