#!/usr/bin/env python3.4
import subprocess, os, re, cgi, cgitb
from os.path import isfile

cgitb.enable()

print('Content-type:text/html')
print()
print('''
<!DOCTYPE html>
<html>
    <head>
        <title>File manager by Vincent_Hawks</title>
    </head>
    <body>
    <table>
    <caption>
''')
form = cgi.FieldStorage()
path = '/var/www/g00/g00u65'
if "path" in form:
    path = form["path"].value
backpath = ''
    
print(path + '''</caption>''')
print('<tr><th>Name</th><th>Type</th></tr>')
if path != '/var/www/g00/g00u65':
    backpath = path[0:path.rindex('/')]
    print('<tr><td><a href="http://g00u65.nn2000.info/cgi-bin/project/lister.py?path=' + backpath + '">Back</a></td><td></td></tr>')

ls = os.listdir(path)


for entry in ls:
    if isfile(path + '/' + entry):
        filepath = path[19:]
        print('<tr><td><a href="http://g00u65.nn2000.info/' + filepath + '/' + entry +'">' + entry + '</a></td><td>File</td></tr>')
    else:
        print('<tr><td><a href="http://g00u65.nn2000.info/cgi-bin/project/lister.py?path=' + path + '/' + entry + '">' + entry + '</a></td><td>Directory</td></tr>')

print('</table>')
print('''<form action="uploader.py" enctype="multipart/form-data" method="post" target="_self">
<p>Upload a file here</p>
<input type="file" name="file">
<input type="hidden" name="path" value="''' + path + '''">
<p><input type="submit" name="Upload"></p></form>''')
print(r'''
    </body>
</html>
''')