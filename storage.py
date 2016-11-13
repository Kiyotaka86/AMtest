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

def adding (names, s_stocks):
    if stocks != None:
        sql = "insert into product values('product', '" + names + "', " + s_stocks + ")"
        cur.execute(sql)

    else:
        sql = "insert into product values('product', '" + names + "', 1)"
        cur.execute(sql)        

def check (names):
    if names ==None:
        sql = "select namae, stock\nfrom product\ngroup product\norder by namae;"
        cur.execute(sql)
        result = cur.fetchall()
        print "Content-type: text/html\n"
        print resut
        
        

if comm != None:
    if comm == 'deleteall':
        sql = "drop table product"
        cur.execute(sql)
        sql = "drop table sales"
        cur.execute(sql)
        sql = "create table product(namae char(50), stock integer)"
        cur.execute(sql)
        sql = "create table sales(namae char(30), sales integer)"
        cur.execute(sql)
        sql = "insert into sales values('sales', 0)"
        cur.execute(sql)
        print "Content-type: text/html\n"
        print ""
    elif comm == 'addstock':
        adding(names, s_stocks)
        print "Content-type: text/html\n"
        print ""
    elif comm == 'checkstock':
        check(names)
    
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

        
