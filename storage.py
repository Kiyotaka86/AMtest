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


def adding (names,  s_stocks):
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
        sql = "select namae, stock from product having stock>0 order by namae;"
        cur.execute(sql)
        result = list(cur.fetchall())
        print "Content-type: text/html\n"
        for f in result:
            print str(f[0]) + ": " + str(f[1])

    else:
        sql = "select namae, stock from product where " + names + ";"
        cur.execute(sql)
        result = list(cur.fetchall())
        print "Content-type: text/html\n"
        for f in result:
            print str([0]) + ": " +str(f[1])

def selling (names, s_stocks, s_kakaku):
    if s_stocks == None:
        if s_kakaku == None:
            sql = "update product set stock=stock-1 where namae='" + names + "';"
            cur.execute(sql)
            print "Content-type: text/html\n"
            print ""
        else:
            sql = "update product set stock=stock-1 where namae='" + names + "';"
            cur.execute(sql)
            sql = "update sales set sales=sales + " + s_kakaku + " where namae='sales';"
            cur.execute(sql)
            print "Content-type: text/html\n"
    else:
        if s_kakaku == None:
            sql = "update product set stock=stock-" + s_stocks + " where namae='" + names + "';"
            cur.execute(sql)
            print "Content-type: text/html\n"
            print ""
        else:
            sql = "update product set stock=stock-" + s_stocks + " where namae=' " + names + "';"
            cur.execute(sql)
            sql = "update sales set sales=sales + " + str(eval(s_kakaku)*eval(s_stocks))  + " where namae='sales';"
            cur.execute(sql)
            print "Content-type: text/html\n"
            print ""
            print ""
            
def checksell():
    sql = "select namae, sales from sales;"
    cur.execute(sql)
    result = list(cur.fetchall())
    print "Content-type: text/html\n"
    for f in result:
        if (isinstance(f[1],(int, long))):
            print str(f[0]) + ": " + str(f[1])
        elif (isinstance(f[1],(float))):
            print str(f[0]) + ": " + str(round(f[1],2))

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
        elif comm == 'checkstock':
        check(names)
    elif comm == 'sell':
        selling(names, s_stocks, s_kakaku)
    elif comm == 'checksales':
        checksell()

connector.commit()

cur.close()
connector.close()


html_body="""
<html><body>
%s
</body></html>"""
