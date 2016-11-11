#!/usr/bin/env python


import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

hen = form.getvalue('foo')

if ' ' in hen or '-' in hen or '*' in hen or '/' in hen:
    if ' ' in hen:
        newhen = hen.replace(' ', '+')
        print "Content-type: text/html\n"
        print eval(newhen)
    else:
        print "Content-type: text/html\n"
        print eval(hen)
else:
    print "Content-type: text/html\n"
    print "ERROR"

html_body="""
<html><body>
%s
</body></html>"""
~                        
