#!/usr/bin/env python3
__author__ = 'fansly'

import mysql.connector, random, string

def generate(num):
    base = string.ascii_letters + string.digits
    a = []
    i = 0
    while i < num:
        code = ''
        for j in range(16):
            code += random.choice(base)
        if code not in a:
            a.append(code)
            i += 1
    print(a)
    return a

def save(a):
    try:
        conn = mysql.connector.connect(user='root', password='admin', database='code')
    except:
        print("failed to connect mysql")
    cursor = conn.cursor()
    cursor.execute('create table  primary key code char(20)')
    for item in a:
        cursor.execute('insert into code values (%s)', [item])
    print('rowcount =', cursor.rowcount)
    conn.commit()
    cursor.close()
    conn.close()

generate(20)

