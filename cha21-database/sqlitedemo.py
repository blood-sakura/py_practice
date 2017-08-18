#!/usr/bin/env python
import sqlite3
sqlite3.threadsafety
cxn = sqlite3.connect('/root/test.db')
cur = cxn.cursor()
cur.execute('select * from user')
for eachUser in cur.fetchall():
    print eachUser

cur.close()
cxn.commit()
cxn.close()