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

print ("ключи(form.keys):",form.keys())
form_keys=list()
form_values=list() 
print  ("Названия ключей   и их значения (как есть)")
i=0
for key in form.keys():
    print  (i,  ": ", key," = ", form.getvalue(key))
    form_keys.append(key)
    i+=1
# сортируем список ключей (что-бы поля не сбоили при выводе в файл)
form_keys.sort() 
print  ("\n","Ключи  и их значения(после сортировки)")
i=0
for form_key in form_keys:
    form_value = form.getvalue(form_key)
    print  (i,  ": ", form_key," = ", form_value)
    form_values.append(form_value)
    i+=1
print(form_keys)
print(form_values)    


if "a_file_name" not in form:
    print ('''
    <form  action="http://g06u33.nn2000.info/cgi-bin/practika.py"   target='_self' method='get'>
    <input type="hidden" name="a_file_name" value="practika.txt" >
    Тип записи в файл:<select name="aa_mode">
        <OPTION value="a">a - дозаписать в файл</OPTION> 
        </select>
    Группа:<select name="005_group">
        <OPTION value="БИ1">БИ1</OPTION> 
        <OPTION value="БИ2">БИ2</OPTION> 
        <OPTION value="БИ3">БИ3</OPTION> 
        </select>
    Фамилия: <input type="Техт" name="012_SecondName" value="" >
    Имя: <input type="Техт" name="014_Name" value="" >
    Отчество <input type="Техт" name="016_SurName" value="" >
    <input type="reset"  name="reset" value="Обновить">
    <input type="submit" name="submit" value="Отправить">
    </form>
    ''')
else:
    print ("\nЗаписываем в файл:", form["a_file_name"].value)
    file = "../tmp/"+form["a_file_name"].value
    if(form["aa_mode"].value=='w'):#0 - очищаем файл 
        file_stream = open(file, mode='w', encoding="utf-8", errors=None)
        file_stream.close()
    file_stream = open(file, mode='a', encoding="utf-8", errors=None)
    for form_key in form_keys:
        form_value = form.getvalue(form_key)
        file_stream.write("%2s ;%2s ;" % (form_key, form_value ))
    file_stream.write("\n")
    file_stream.close()
    print ("\nЗаписано в:", file)
    print("\nСчитываем данные из файла и обрабатываем")
    r_stream = open(file, mode='r', encoding="utf-8")
    for line in r_stream.readlines():
        print ('line: ',line,end='')
        words = line.split("; ")
        #print ("words:\n",words)

    print('''
</pre>
</body>
<html>
''')