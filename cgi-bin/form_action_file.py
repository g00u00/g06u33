#!/usr/bin/env python3.4
import os,sys
import cgi, cgitb
import form_action_functions_file

cgitb.enable()

form = cgi.FieldStorage()

def form_action_file(form):
    print("\n<pre>") 
    print("\n\nform_dict = ",form_action_functions_file.form_dictionary(form)) #Анализируем строку запроса
    form_action_functions_file.print_form_file(form) #Создаем форму и отправляем данные на сервер
    form_action_functions_file.file_list(form) #Записываем в файл и оцениваем содержание файла 
    print("\n</pre>")

def form_action_file_bash(form):
    print("\n<pre>")
    print("\nОбрабатываем уникальную форму\n") 
    #form_action_functions_file.form_dictionary(form) #Анализируем строку запроса
    #form_action_functions_file.print_form_file(form) #Создаем форму и отправляем данные на сервер
    form_action_functions_file.file_list_bash(form) #Записываем в файл и оцениваем содержание файла 
    print("\n</pre>")


if __name__=='__main__':
    print("Content-type:text/html\r\n")
    print(
    "<html>\n",
    "<head>\n<title>Отладка, в файл, из файла, обработка </title>\n</head>\n",
    "\n<body>\n<h3>Отладка, в файл, из файла, обработка</h3>\n",
    )
    if "ls" not in form:
        form_action_file(form)
    else:
        form_action_file_bash(form)
