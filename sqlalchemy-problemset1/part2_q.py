import sqlite3
conn = sqlite3.connect("C:\\~\\Documents\\sqlalchemy-problemset1\\sailors.db")

c = conn.cursor()
c.execute('SELECT * FROM sailors') #testing out the way it works
#print c.fetchall()

c.execute('SELECT * FROM reserves')
#print c.fetchall()

c.execute('SELECT * FROM boats')
#print c.fetchall()

c.execute('SELECT DISTINCT b.bname, s.sname, COUNT(*) FROM boats b, reserves r, sailors s WHERE b.bid = r.bid AND s.sid = r.sid GROUP BY b.bid, b.bname, s.sid, s.sname HAVING COUNT(*) >= (SELECT COUNT(*) FROM reserves r1 WHERE r1.bid = b.bid GROUP BY r1.sid)')
print c.fetchall() #Question 1

c.execute('SELECT b.bid, COUNT(*) as reservescount FROM boats b, reserves r WHERE r.bid = b.bid GROUP BY b.bid HAVING COUNT(*) > 0')
print c.fetchall() #Question 2

c.execute('SELECT s.sid, s.sname, COUNT(*) as reservescount FROM sailors s, reserves r, boats b WHERE s.sid = r.sid AND r.bid = b.bid AND b.color = "red" GROUP BY s.sid HAVING COUNT(*) > 1')
print c.fetchall() #Question 3

c.execute('SELECT b.bid, b.bname, COUNT(*) FROM boats b, reserves r WHERE b.bid = r.bid GROUP BY b.bid, b.bname HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM reserves r1 GROUP BY r1.bid)')
#print c.fetchall()

c.execute('SELECT * FROM sailors s WHERE s.sid NOT IN (SELECT r.sid FROM reserves r WHERE r.bid IN (SELECT b.bid FROM boats b WHERE b.color = "red"))')
print c.fetchall() #Question 6

c.execute('SELECT AVG(s.age) FROM sailors s WHERE s.rating = 10')
print c.fetchall() #Question 7
