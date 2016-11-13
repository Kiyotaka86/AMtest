#!/usr/bin/env python

import cgi, cgitb, MySQLdb
cgitb.enable()

connector = MySQLdb.connect(host="localhost", db="stocker", user="kio", passwd="kio")
cur=connector.cursor()

form = cgi.FieldStorage()

comm = form.getvalue('function')
names = form.getvalue('name')
s_stocks = form.getvalue('amount')
s_kakaku = form.getvalue('price')

stocks = None
kakaku = None

if comm != None:
    if comm == 'deleteall'
        sql = "drop table product"
        cur.execute(sql)
        sql = "create table product(shurui char(10), namae char(50), stock integer)"
        cur.execute(sql)

if s_stocks != None:
    if (isinstance(eval(s_stocks),(int, long))):
        stocks = eval(s_stocks)
    else:
        print "Content-type: text/html\n"
        print "ERROR"
if s_kakaku != None:
    if (isinstance(eval(s_kakaku),(int, long))):
       kakaku = eval(s_kakaku)
    else:
        print "Content-type: text/html\n"
        print "ERROR"

connector.commit()


cur.close()
connector.close()


html_body="""
<html><body>
%s
</body></html>"""

        
