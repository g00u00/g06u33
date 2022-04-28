#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
#cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type:text/html\r\n
<html>
<head>
    <title>Hello Word</title>
    <meta http-equiv="Content-Type" CONTENT="text/html; charset=utf-8">
</head>

<body>
''')

cgi.test()
print(cgi.FieldStorage())
form = cgi.FieldStorage()
#print(form) 

query = os.environ[ "QUERY_STRING" ]
print("\n\nСтрока обработана cgi.parse_qs(query): ", cgi.parse_qs(query))

#изучение и тестирование
print ("\n\nform.keys:",form.keys())
i=0
for key in form.keys():
   variable = str(key)
   value = str(form.getvalue(variable))
   print  (str(i) +  "-" + variable +":"+ value)
   i+=1
print ("\n\n")


print('''\
</body>
</html>
''')
