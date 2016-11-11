#!/usr/bin/env python


import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

shiki = form["foo".value
#shiki = eval(form.getvalue('foo'))

#result = eval(shiki)

print "Content-type: text/html\n"
print shiki

html_body="""
<html><body>
%s
</body></html>"""
