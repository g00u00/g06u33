#!/usr/bin/env python3

import os,sys
import cgi, cgitb
import form_action_functions_file
cgitb.enable()
form = cgi.FieldStorage()


def form_dictionary(form):
    print ("Анализ строки запроса")
    print ("ключи(form.keys):",form.keys())
    form_keys_list=list()
    form_values_list=list() 
    form_dict=dict() 
    print  ("Названия ключей  и их значения (как есть)")
    i=0
    for form_key in form.keys():
        print  (i,  ": ", form_key," = ", form.getvalue(form_key))
        form_keys_list.append(form_key)
        form_values_list.append(form.getvalue(form_key))
        form_dict.update({form_key: form.getvalue(form_key)})
        i+=1
    
    print('\nВ виде словаря (form_dict):\n', form_dict)

    # сортируем список ключей (что-бы поля не сбоили при выводе в файл)
    print  ("\n\nКлючи  и их значения после сортировки ")
    form_keys_list.sort()
    i=0
    for form_key in form_keys_list:
        print  (i,  ": ", form_key," = ", form.getvalue(form_key))
        i+=1
    print("form_keys_list: ", form_keys_list)
    return(form_dict)


def file_list(form):
    form_keys_list=list()
    for form_key in form.keys():
        form_keys_list.append(form_key)
    form_keys_list.sort()
    if "000_file_name" in form:
        file = "../tmp/" + form["000_file_name"].value
        print ("\n\nЗаписываем в: ", os.environ[ "HTTP_HOST" ], file[2:], sep= '')
        if(form["010_mode"].value=='w'):#0 - очищаем файл 
            file_stream = open(file, mode='w', encoding="utf-8", errors=None)
            file_stream.close()
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)
        for form_key in form_keys_list:
            form_value = form.getvalue(form_key)
            file_stream.write("%1s;%1s;" % (form_key, form_value ))
            sys.stdout.write("%1s;%1s;" % (form_key, form_value ))
        file_stream.write("\n")
        file_stream.close()

        listB = list() #для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print ("\n\nПострочно считываем строки из ", os.environ[ "HTTP_HOST" ] , file[2:], "\nи разбираем на слова\n", sep='')
        for line in r_stream.readlines():
            words = line.split(";")
            print(words)
#            listB.append(words[5])
#        print("\nlistB(Список из столбца с ключом variable_3):", listB)
#        print("listB.__len__():", listB.__len__())



print('''\
Content-type:text/html\r\n
<html>
<head>\n<title>Форма, строка запроса, запись и считывание</title>\n</head>
<body>\n<pre>
''')
form_dictionary(form) #Анализируем строку запроса
file_list(form) #Записываем в файл и оцениваем содержание файла 


print('\n</pre>\n</body>\n<html>')
