#!/usr/bin/env python


import cgi

form = cgi.FieldStorage()



print "Content-type: text/html\n"
print form.getvalue('foo')

html_body="""
<html><body>
%s
</body></html>"""
