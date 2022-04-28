#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
import form_action_functions
cgitb.enable()
sys.stderr = sys.stdout
form = cgi.FieldStorage()

print('''\
Content-type:text/html\r\n
<html>
<head>\n<title>Форма, строка запроса, запись и считывание</title>\n</head>
<body>\n<pre>
''')

print ("\nform_action_functions.form_dictionary(form):\n", form_action_functions.form_dictionary(form)) #Анализируем строку запроса
print("\nform_action_functions.file_list(form):\n", form_action_functions.file_list(form)) #Записываем в файл и оцениваем содержание файла 
print("\nprint_form():\n", form_action_functions.print_form()) #Создаем форму и отправляем данные на сервер

print('\n</pre>\n</body>\n<html>')
