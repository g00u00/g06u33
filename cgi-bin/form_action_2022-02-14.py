#!/usr/bin/env python3

def form_dictionary():
    import os, sys
    import time, datetime
    import cgi, cgitb
    cgitb.enable()
    form = cgi.FieldStorage()
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
        i+=1

    # сортируем список ключей (что-бы поля не сбоили при выводе в файл)
    print  ("\n\nКлючи  и их значения после сортировки ")
    form_keys_list.sort()
    i=0
    for form_key in form_keys_list:
        print  (i,  ": ", form_key," = ", form.getvalue(form_key))
        form_values_list.append(form.getvalue(form_key))
        form_dict.update({form_key: form.getvalue(form_key)})
        i+=1
    print("form_keys_list: ", form_keys_list)

    form_dict.update({"REMOTE_ADDR": os.environ[ "REMOTE_ADDR" ]})
    form_dict.update({"date": time.strftime('%Y-%m-%d')})
    print('\nВ виде словаря (form_dict) с дополнениями:\n', form_dict)
    return(form_dict)


def file_write_read(my_dict):
    import os, sys
    import json
    my_dict_keys_list = my_dict.keys()
    print (my_dict_keys_list)

    if "000_file_name" in my_dict_keys_list:
        file = "../tmp/" + my_dict.get('000_file_name')
        print (file)
        print ("\n\nЗаписываем в: ", os.environ[ "HTTP_HOST" ], file[2:], sep= '')
        if(my_dict.get("010_mode")== 'w'):#0 - очищаем файл
            file_stream = open(file, mode='w', encoding="utf-8", errors=None)
            file_stream.close()
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)
        for form_key in my_dict_keys_list:
            form_value = my_dict.get(form_key)
            file_stream.write("%1s:%1s," % (form_key, form_value ))
            sys.stdout.write("%1s:%1s," % (form_key, form_value ))
        file_stream.write("\n")
        file_stream.close()
        listB = list() #для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print ("\n\nПострочно считываем строки из ", os.environ[ "HTTP_HOST" ] , file[2:], " и разбираем на пары\n", sep='', end='')
        for line in r_stream.readlines():
            print (line, end='')
            words = line.split(",")
            print(words,'\n')

    list_age = []
    if "000_file_name" in my_dict_keys_list:
        file = "../tmp/" + my_dict.get('000_file_name') + ".json"
        print ("\n\nЗаписываем в: ", os.environ[ "HTTP_HOST" ], file[2:], sep= '')
        if(my_dict.get("010_mode")== 'w'):#0 - очищаем файл
            file_stream = open(file, mode='w', encoding="utf-8", errors=None)
            file_stream.close()
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)
        file_stream.write(json.dumps(my_dict, ensure_ascii=False))
        sys.stdout.write(json.dumps(my_dict, ensure_ascii=False))
        file_stream.write("\n")
        file_stream.close()
        listB = list() #для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print ("\n\nПострочно считываем строки из ", os.environ[ "HTTP_HOST" ] , file[2:], "и разбираем на пары", sep='')
        for line in r_stream.readlines():
            print(line, end='')
            new_dict =  json.loads(line)
            print(new_dict, '\n')
            list_age.append(new_dict.get('age'))
        print(list_age)




print('''\
Content-type:text/html\r\n
<html>
<head>\n<title>Форма, строка запроса, запись и считывание</title>\n</head>
<body>\n<pre>
''')
result = form_dictionary()#Анализируем строку запроса
print('\nФункция вернула:\n', result, '\n')
file_write_read(result) #Записываем в файл и оцениваем содержание файла


print('\n</pre>\n</body>\n<html>')
