#!/usr/bin/env python3.4
#https://stackoverflow.com/questions/36484184/python-make-a-post-request-using-python-3-urllib
import time, datetime
import os,sys
import requests
#from http import cookies
import cgi, cgitb
#cgitb.enable()
from urllib import request, parse



res = requests.get('http://yandex.ru')

url = 'http://g06u33.nn2000.info'

#headers1 = {'user-agent': 'your-own-user-agent/0.0.1'}
#cookies1 = {'visit-month': 'February'}
#req = requests.get(url, headers=headers1, cookies=cookies1)
#cookies = {'visit-month': 'February'}
cookies1 = {'visit-month1': 'February1', 'visit-month2': 'February2', 'visit-month3': 'February3'}
#cookies = dict(cookies_are='working')
#requestsJar = requests.cookies.RequestsCookieJar()
#requestsJar.set("user10","user20", domain="abc1", path="abc2")
#req = requests.post(url, cookies-requestsJar)
#req1 = requests.get(url, cookies=cookies1)

data1=cookies1
data2 = parse.urlencode(cookies1).encode()

req1 = requests.get(url, data=data1)
req2 = requests.get(url)


req3 =  request.Request('http://g06u33.nn2000.info', data=data2) # this will make the method "POST"
#req3.add_header('Content-Type', 'application/json')
req3.add_header('переменная1','значение1')
req3.add_header('переменная2','значение2')


print('''\
Content-type:text/html\r\n


<!DOCTYPE html>\n<html>\n<head>\n<title>g06u33_CGI_тестируем</title>\n</head>
<body>\n<pre>
Html-страница сгенерирована
''')



print("\nres:")
print(res)
print(res.status_code)
print(res.headers)
print(res.cookies)
#print(res.text)
print(res.url)



print('\nreq1')
print(req1)
print(req1.status_code)
print(req1.headers)
print(req1.cookies)
print(req1.text)
print(req1.url)


print('\nreq2')
print(req2)
print(req2.status_code)
print(req2.headers)
print(req2.cookies)
print(req2.text)
print(req2.url)


print('\nreq3')
print(req3)
print(req3._data)
print(req3.full_url)
print(req3.headers)


#cgi.test()
print("\n\n",os.environ[ "REMOTE_ADDR" ])
print(cgi.FieldStorage())
qr_string = cgi.FieldStorage()
print ("\n\nqr_string.keys:",qr_string.keys())
i=0
for key in qr_string.keys():
    var_name = str(key)
    var_value = str(qr_string.getvalue(var_name))
    print  (str(i) +  ":" + var_name +"="+ var_value)
    i+=1
print ("\n\n")
print ("\nfunc_value=", qr_string.getvalue("func"))

print('''\
<pre>\n<body>\n<html>
''')