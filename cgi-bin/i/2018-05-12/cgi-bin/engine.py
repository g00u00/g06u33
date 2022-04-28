#!/usr/bin/env python3.4
#http://g01u00.nn2000.info/cgi-bin/engine.py?info_file=../public_html/page_1/info.htm

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type:text/html\r\n
<html>
<head>
    <title>Hello Word</title>
    <meta http-equiv="Content-Type" CONTENT="text/html; charset=utf-8">
    <link rel="stylesheet" href="../css/engine.css">
</head>
<body>
''')

form = cgi.FieldStorage()
info_file = form.getvalue('info_file')
if "info_file" not in form:
    info_file="../public_html/page_1/info.htm"


print ('''
<div>
<div  class="hellobox">
<h1>''')      
with open('../public_html/hello/info.htm', mode='r', encoding="utf-8", errors=None) as f_read:
    for line in f_read: print (line)
print ('''
</h1>
</div>
<ul>''')

print ('''
<nav>
<ul>''')
with open('../public_html/navigation/info.htm', mode='r', encoding="utf-8", errors=None) as f_read:
    for line in f_read: print (line)
print ('''
</ul>
</nav>
''')
    
print ('''<section>''')
#print (info_file)
with open(info_file, mode='r', encoding="utf-8", errors=None) as f_read:
    for line in f_read: print (line)
print ('''</section>
''')

print ('''<footer>''')    
with open('../public_html/footer/info.htm', mode='r', encoding="utf-8", errors=None) as f_read:
    for line in f_read: print (line)
print ('''
</footer>
''')
print ('''
</div>
</body>
</html>
''')
