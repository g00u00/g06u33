#!/usr/bin/env python3.4
import os, pwd, datetime 
#import development_file #импортируем модуль development_file.py

def development(): 
    print("<pre>")
    print("Исполнитель, место и время исполнения")
#
#    print(os.environ['USER'])  #ssh
#    print(os.environ['PWD']) #ssh
#
    print("Сайт: ",os.environ['HTTP_HOST']) #http
    print("Раздел на сервере: ", os.environ['CONTEXT_DOCUMENT_ROOT']) #http
    print("Адрес клиента: ", os.environ['REMOTE_ADDR']) #http
#
    print("Дата и время исполнения: ", datetime.datetime.today().strftime('%Y-%m-%d %H:%M'))
    print("</pre>")

    
print('''\
Content-type:text/html\r\n
<!DOCTYPE html>
<html>
<head>
<title>Заголовок</title>
</head>
<body>
''')

#О разработчике
print("\n<pre>")
#development_file.development()
development()
print("\n<pre>")
#

#Оформление лабораторных
print("Формулировка задачи(источник, страница, номер задачи , текст задачи)")
print('''\
...
''')
print("\n\nТекст программы")
print('''\
...
''')
print("\n\nСодержание файла исходных данных программы")
print('''\
...
''')

print("\n\nРешение задачи(интерфейс работающей программы)")
print('''\
...
''')
print("\n\nСодержание файла с результатами")
print('''\
...
''')
print("</pre>")
