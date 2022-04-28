#!/usr/bin/env python3.4
#http://g06u33.nn2000.info/cgi-bin/engine.py?info_file=../public_html/form/info.htm

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

if "exp" in form:  
    print('\n\n Список в строке: запроса ', form.getvalue('exp'))
    strExp = form.getvalue('exp')
    intList = list()
    for item in strExp: intList.append(int(item))
    print(intList, sum(intList)) 


if "000_file_name" not in form:
    print ('''
    <form  action="http://g06u33.nn2000.info/cgi-bin/form_action.py"  method='get' target='_self'>
    Название файла: <input type="Техт" name="000_file_name" value="g06u33.txt" >
    Тип записи в файл:<select name="010_mode">
        <OPTION value="a">a - дозаписать в файл</OPTION> 
        <OPTION value="w">w - очисить файл и записать в файл</OPTION> 
        </select>
    Первая переменная: <input type="Техт" name="name" value="Иван" >
    Вторая переменная: <input type="Техт" name="exp" value="30" >
    <input type="reset"  name="reset" value="Обновить">
    <input type="submit" name="submit" value="Отправить">
    </form>
    ''')
else:
    print ("\n\nЗаписываем в файл:", form["000_file_name"].value)
    file = "../tmp/"+form["000_file_name"].value
    if(form["010_mode"].value=='w'):#0 - очищаем файл 
        file_stream = open(file, mode='w', encoding="utf-8", errors=None)
        file_stream.close()
    file_stream = open(file, mode='a', encoding="utf-8", errors=None)
    for form_key in form_keys:
        form_value = form.getvalue(form_key)
        file_stream.write("%2s ;%2s ;" % (form_key, form_value ))
    file_stream.write("\n")
    file_stream.close()
    print ("\nЗаписано в:", file)

    #Будем получать и обрабатывать данные из файла
    #формируем списки для анализа данных
    a = list()
    print("\nСчитываем данные из файла и обрабатываем")
    r_stream = open(file, mode='r', encoding="utf-8")
    for line in r_stream.readlines():
        print ('\nline: ',line,end='')
        words = line.split(";")
        a.append(words[1])
    print(a)
    print('''
</pre>
</body>
<html>
''')
