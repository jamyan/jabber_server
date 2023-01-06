#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from sshtunnel import SSHTunnelForwarder

server_jabber = SSHTunnelForwarder(
    ('172.16.1.85', 2234),
    ssh_username='root',
    ssh_password='Sj9Ls&;!',
    remote_bind_address=('127.0.0.1', 3306)
)
server_jabber.start()
con = pymysql.connect(host='127.0.0.1', user='root', passwd='Sj9Ls&;!', db='jabber', port=server_jabber.local_bind_port)

with con:
    cur = con.cursor()

    userlist = open('userlist.txt', 'r')
    users = userlist.readlines()
    for user in users:
        print(user)
        user = user.rstrip('\n')
        sql1 = r'DELETE FROM ofUser WHERE username="{}";'.format(user)
        sql2 = r'DELETE FROM ofUserProp WHERE username="{}";'.format(user)
        sql3 = r'DELETE FROM ofGroupUser WHERE username="{}";'.format(user)
        sql4 = r'DELETE FROM ofRoster WHERE username="{}";'.format(user)
        sql5 = r'DELETE FROM ofUserFlag WHERE username="{}";'.format(user)
        sql6 = r'DELETE FROM ofOffline WHERE username="{}";'.format(user)
        cur.execute(sql1)
        cur.execute(sql2)
        cur.execute(sql3)
        cur.execute(sql4)
        cur.execute(sql5)
        cur.execute(sql5)
    userlist.close()

    con.commit()