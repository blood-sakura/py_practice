#!/usr/bin/env python

import MySQLdb
import datetime

# MySQLdb.paramstyle = "qmark"

cxn = MySQLdb.connect(host='localhost', user='root')
cxn.query('DROP DATABASE test')
cxn.query('CREATE DATABASE test')
cxn.query("GRANT ALL ON test.* to ''@'localhost'")
cxn.commit()
cxn.close()

now = datetime.datetime(2009, 5, 5, 20, 31, 44).strftime('%Y-%m-%d %H:%M:%S')

cxn = MySQLdb.connect(host='localhost', user='root', db='test')
cur = cxn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8), uid INT, ct TIMESTAMP, at DATETIME)')
cur.execute("INSERT INTO users VALUES(%s, %s, %s, %s)", ('Peter', 7000, now, now))
cur.execute("INSERT INTO users VALUES(%s, %s, %s, %s)", ('Jane', 7001, now, now))
cur.execute("INSERT INTO users VALUES(%s, %s, %s, %s)", ('Bob', 7002, now, now))

cur.execute("SELECT * FROM users")

for data in cur.fetchall():
    print "%s\t%s\t%s\t%s" % data

cur.execute('DELETE FROM users WHERE login="Bob"')
cur.execute('DROP TABLE users')

cur.close()
cxn.commit()
cxn.close()