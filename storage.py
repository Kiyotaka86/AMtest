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

ef adding (names,  s_stocks):
    stocks =None
    if s_stocks != None:
        if (isinstance(eval(s_stocks),(int, long))):
            stocks = eval(s_stocks)
            sql = "insert into product values('" + names + "', " + s_stocks + ")"
            cur.execute(sql)
            print "Content-type: text/html\n"
            print ""
        else:
            print "Content-type: text/html\n"
            print "ERROR"
    else:
        sql = "insert into product values('" + names + "', 1)"
        cur.execute(sql)
        print "Content-type: text/html\n"
        print ""
    
 

def check (names):
    if names == None:
        sql = "select namae, stock from product order by namae;"
        cur.execute(sql)
        result = list(cur.fetchall())
        print "Content-type: text/html\n"
        for f in result:
            print f[0]
            print ":"
            print f[1]
            print "<BR>"

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
    
        
        
connector.commit()


cur.close()
connector.close()


html_body="""
<html><body>
%s
</body></html>"""

        
