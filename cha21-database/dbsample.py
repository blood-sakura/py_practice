#!/usr/bin/env python

import os
from random import randrange as rrange

COLSIZ = 10
RDBMSs = {'s':'sqlite', 'm':'mysql'}
DB_EXC = None

def setup():
    return RDBMSs[raw_input('''
Choose a database system:
    (M)ySQL
    (S)QLite

Enter choice:''').strip().lower()[0]]

def connect(db, dbName):
    global DB_EXC
    dbDir = '%s_%s'%(db, dbName)
    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError, e:
            return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
            cxn = sqlite3.connect(os.path.join(dbDir, dbName))

    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC
        except ImportError, e:
            return None

        try:
            cxn = MySQLdb.connect(db=dbName)
        except DB_EXC.OperationalError, e:
            cxn = MySQLdb.connect(user='root')
            try:
                cxn.query('DROP DATABASE %s' % dbName)
            except DB_EXC.OperationalError, e:
                pass

            cxn.query('CREATE DATABASE %s' % dbName)
            cxn.query("GRANT ALL ON %s.* to ''@'localhost'" % dbName)
            cxn.commit()
            cxn.close()
            cxn = MySQLdb.connect(db=dbName)

    else:
        return None
    return cxn

def create(cur):
    try:
        cur.execute('''
        CREATE TABLE users (
            login VARCHAR(8),
            uid INTEGER,
            prid INTEGER)
        ''')
    except DB_EXC.OperationalError, e:
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
    ('aaron', 8312), ('angela', 7603), ('dave', 7306),
    ('davina', 7902), ('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('sereba', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209)
)

def randName():
    pick = list(NAMES)
    while len(pick) > 0:
        yield pick.pop(rrange(len(pick)))