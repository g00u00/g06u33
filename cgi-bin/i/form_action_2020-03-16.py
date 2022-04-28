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
form_keys_list=list()
form_values_list=list() 
form_values_dict=dict() 
print  ("Названия ключей  и их значения (как есть)")
i=0
for form_key in form.keys():
    print  (i,  ": ", form_key," = ", form.getvalue(form_key))
    form_keys_list.append(form_key)
    form_values_list.append(form.getvalue(form_key))
    form_values_dict.update({form_key: form.getvalue(form_key)})
    i+=1
print('\nВ виде словаря (form_values_dict):\n', form_values_dict)
# сортируем список ключей (что-бы поля не сбоили при выводе в файл)
print  ("\n","Ключи  и их значения после сортировки ")
form_keys_list.sort()
i=0
for form_key in form_keys_list:
    print  (i,  ": ", form_key," = ", form.getvalue(form_key))
    i+=1
print("form_keys_list: ", form_keys_list)
print("form_keys_list: ", form_values_list) 


if "experience" in form:  
    print('\n\n Пример списка из строки запроса (experience): ', form.getvalue('experience'))
    strExperiences = form.getvalue('experience')
    print("strExperiences: ", strExperiences)
    intExperiences = list()
    for item in strExperiences: intExperiences.append(int(item))
    print("intExperiences: ", intExperiences, "   sum(intExperiences): ", sum(intExperiences)) 


if "000_file_name" in form:
    print ("\n\nЗаписываем в файл:", form["000_file_name"].value)
    file = "../tmp/"+form["000_file_name"].value
    if(form["010_mode"].value=='w'):#0 - очищаем файл 
        file_stream = open(file, mode='w', encoding="utf-8", errors=None)
        file_stream.close()
    file_stream = open(file, mode='a', encoding="utf-8", errors=None)
    for form_key in form_keys_list:
        form_value = form.getvalue(form_key)
        file_stream.write("%1s;%1s;" % (form_key, form_value ))
    file_stream.write("\n")
    file_stream.close()
    print ("\nЗаписано в:", file)

    listB = list()
    r_stream = open(file, mode='r', encoding="utf-8")
    print ("\nПострочно считываем из :", file)
    for line in r_stream.readlines():
        print (line,end='')
        words = line.split(";")
        print(words)
        listB.append(words[1])
    print("\nlistB(Список, сфомирован из 2-го столбца файла):\n", listB)

print ('''
<form  action="http://g06u33.nn2000.info/cgi-bin/form_action.py"  method='get' target='_self'>
Название файла: <input type="Техт" name="000_file_name" value="g06u33.txt" >
Тип записи в файл:<select name="010_mode">
    <OPTION value="a">a - дозаписать в файл</OPTION> 
    <OPTION value="w">w - очисить файл и записать в файл</OPTION> 
    </select>
Первая переменная: <input type="Техт" name="name" value="Иван" >
Вторая переменная: <input type="Техт" name="experience" value="30" >
<input type="reset"  name="reset" value="Обновить">
<input type="submit" name="submit" value="Отправить">
</form>
''')
print('\n</pre>\n</body>\n<html>')
