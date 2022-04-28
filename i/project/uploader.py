#!/usr/bin/env python3.4
#coding: utf-8

import cgi, cgitb, requests
cgitb.enable()

print('Content-type:text/html')
print()
print('''
<!DOCTYPE html> 
<html> 
    <head> 
        <title>Uploader</title> 
    </head> 
    <body>''')

form = cgi.FieldStorage()
if not "file" in form:
    print('<h1>Oops! Something went wrong</h1>')
    print('<p>File is empty or has not been transfered</p>')
    
elif not "path" in form:
    print('<h1>Oops! Something went wrong</h1>')
    print('<p>File path has not been received. Try reuploading, if this message comes up again, please contact me.</p>')
    
else:
    file = form["file"].value
    name = form["file"].filename
    path = form["path"].value
    try:
        save = open(path + '/' + name, mode = 'wb')
        save.write(file)
        save.close()
        print('<p>Upload successful</p>')
    except UnicodeEncodeError:
        print('<h1>Oops! Something went wrong</h1>')
        print('<p>Please rename the uploaded file in ASCII characters and try again</p>')
    except PermissionError:
        print('<h1>Oops! Something went wrong</h1>')
        print('<p>You are not allowed to upload here. Go upload somewhere else or become allowed, i don\'t know</p>')
    
print('''<form action="lister.py" target="_self" method="get">
<input type="hidden" name="path" value="''' + form["path"].value + '''">
<input type="submit" name="Back" value="Back">
</form>''')
    
print('''
    </body> 
</html>
''')