#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
import form_functions

cgitb.enable()

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
print  ("\nНазвания ключей   и их значения (как есть)")
i=0
for key in form.keys():
    print  (i,  ": ", key," = ", form.getvalue(key))
    form_keys.append(key)
    i+=1

if "000_file_name" in form:
    print ("\n000_file_name: ", form["000_file_name"].value)
    print ("010_mode: ", form["010_mode"].value)
    print ("variable1: ", form["variable1"].value)
    print ("variable2: ", form["variable2"].value)

    try:
        variable1 = int(form["variable1"].value)
        variable2 = float(form["variable2"].value)
    except Exception as mistake:
        print("\n\nОшибка ввода")
        print(mistake)
    else:
      print('\n\nОшибки нет, вызываем функцию (при необходимости)')
      print(form_functions.function_1(variable1, variable2))

print ('''
<form  action="./form.py"   target='_self' method='get'>
Название файла: <input type="Техт" name="000_file_name" value="qs_file.txt" >
Тип записи в файл:<select name="010_mode">
    <OPTION value="a">a - дозаписать в файл</OPTION> 
    <OPTION value="w">w - очисить файл и записать в файл</OPTION> 
    </select>
Первая переменная: <input type="Техт" name="variable1" value="100 or Иван" >
Вторая переменная: <input type="Техт" name="variable2" value="1990. or Иванов" >
<input type="reset"  name="reset" value="Обновить">
<input type="submit" name="submit" value="Отправить">
</form>
''')

print('''
</pre>
</body>
<html>
''')
