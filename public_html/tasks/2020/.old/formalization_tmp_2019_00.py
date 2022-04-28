#!/usr/bin/env python3.4
import os, sys,  pwd, datetime
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout 

#import development_file #импортируем модуль development_file.py
def development(): #Функцию не изменять
    print("<pre>")
    print("Исполнитель, место и время исполнения")
#    print(os.environ['USER'])  #ssh
#    print(os.environ['PWD']) #ssh
    print("Сайт: ",os.environ['HTTP_HOST']) #http
    print("Раздел на сервере: ", os.environ['CONTEXT_DOCUMENT_ROOT']) #http
    print("IP посетителя: ", os.environ['REMOTE_ADDR']) #http
    print("Дата и время исполнения программы: ", datetime.datetime.today().strftime('%Y-%m-%d %H:%M'))
    print("</pre>")
    
print('''\
Content-type:text/html\r\n
<!DOCTYPE html>
<html>
<head>\n<title>Лабораторная работа №1</title>\n</head>
<body>
''')
print("\n<pre>")

#О разработчике
#development_file.development()
development()
#Оформление лабораторных
print("Формулировка задачи(источник, страница, номер задачи , текст задачи)")
print('''\
...
''')

print("\n\nСодержание файла исходных данных программы")
print('''\
...
''')

print("\n\nРешение задачи(интерфейс работающей программы)")
#Заменить представленный фрагмент свой программой
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
if "last_name" in form:
    print ("\nБыли введены следующие данные:")
    print ("Фамилия:", form["last_name"].value)
    print ("Год рождения:", form["year_of_birth"].value)
    print ("Опыт работы:", form["experience"].value)
print ('''
<form  action="formalization.py"   target='_self' method='get'>
Введите новые данные
Фамилия: <input type="Text" name="last_name" value=""   size=8 >
Год рождения: <input type="Text" name="year_of_birth" value=""   size=8 >
Опыт работы: <input type="Text" name="experience" value=""   size=8 >
<input type="Submit" name="Submit" value="Отправить_данные_на_сервер">
''')
#конец представленного фрагмента

print("\n\nСодержание файла с результатами")
print('''\
...
''')
print("</pre>")
