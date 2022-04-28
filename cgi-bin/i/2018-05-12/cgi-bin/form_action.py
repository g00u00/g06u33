#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type:text/html\r\n
<html>
<head>
<title>Форма, строка запроса, запись и считывание</title>
</head>
<body>
<pre>
''')
form = cgi.FieldStorage()

'''
print ("form.keys:",form.keys())
i=0
for key in form.keys():
    variable = str(key)
    value = str(form.getvalue(variable))
    print  (str(i) +  "-" + variable +":"+ value)
    i+=1
print ("\n")
'''

if "last_name" not in form:
    print ('''
    <form  action="form_action.py"   target='_self' method='get'>
    Введите данные
    Фамилия: <input type="Text" name="last_name" value=""   size=8 >
    Год рождения: <input type="Text" name="year_of_birth" value=""   size=8 >
    Опыт работы: <input type="Text" name="experience" value=""   size=8 >
    <input type="Submit" name="Submit" value="Отправить_данные_на_сервер">
    ''')

else:
    print ("Фамилия:", form["last_name"].value)
    print ("Год рождения:", form["year_of_birth"].value)
    print ("Опыт работы:", form["experience"].value)
    
    with open('../tmp/file.txt', mode='a', encoding="utf-8", errors=None, newline=None, closefd=True, opener=None) as f_append:
        f_append.write("%2s %3i %3.1f\n" % (str(form["last_name"].value), int(form["year_of_birth"].value), float(form["experience"].value) ))
    
    a=list()
    b=list()
    c=list()
    d=list()
    i=0
    my_sum=0
    
    print("\nСчитываем данные из файла и обрабатываем")
    with open('../tmp/file.txt', mode='r', encoding="utf-8") as f_read:
        for line in f_read.readlines():
            print ('\n',line,end='')
            words = line.split()
            print (words)
'''            a.insert(0,words[0])
            b.insert(0,words[1])
            c.insert(0,words[2])
            d.insert(0,float(words[1])*float(words[2]))
            print (a,b,c,d)
            my_sum+=float(words[1])*float(words[2])
            i+=1
        print (my_sum)        
        print ("Свойства ...")
        print(d)
        print (type(d))
        print (d.__len__())
        print (d.__sizeof__())
        print (d.count('34000.0'))
        print(sum(d))
        print(max(d))
        print(min(d))
        d.sort()
        print(d)
 '''       
'''     print(line)
        print(line.split())
        [x,y,z]=line.split()
        print (x,y,z)
''' 
print('\n</pre>\n</body>\n<html>')
