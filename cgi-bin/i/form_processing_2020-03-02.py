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
'''
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
'''

if "file_name" not in form:
    print ('''
    <form  action="form_processing.py"   target='_self' method='get'>
    Введите данные
    Наименование: <input type="Text" name="qs_name" value=""   size=20 >
    Цена: <input type="Text"  name="qs_price" value="0.00"    size=6 >
    Количество: <input type="Text"  name="qs_amount" value="0"    size=6 >
    Тип действий:<select name="qs_type">
        <OPTION value="Доходы">Доходы</OPTION> 
        <OPTION value="Расходы">Расходы</OPTION> 
        <OPTION value="w">Удаление данных</OPTION> 
        </select>
    <br><br><br>
    <input type="Hidden" name="file_name" value="qs_file.txt" >
    <input type="reset"  name="reset" value="Обновить">
    <input type="submit" name="submit" value="Отправить">
    </form>
    ''')
else:
    qs_name = form["qs_name"].value
    qs_price = form["qs_price"].value
    qs_amount = form["qs_amount"].value
    qs_type = form["qs_type"].value
    file_name = form["file_name"].value
    print ("\n\nНаименование:", qs_name)
    print ("Цена:", qs_price)
    print ("Количество:", qs_amount)
    print ("Тип:", qs_type)
    file = "../tmp/"+file_name
    print ("\nРаботаем с файлом:", file)
    if(qs_type=='w'):#w - очищаем файл 
        file_stream = open(file, mode='w', encoding="utf-8", errors=None)
        file_stream.close()
    else:#a - дозаписываем в файл 
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)
        file_stream.write("%2s;%3.2f;%1i;%1s;\n" % (str(qs_name), float(qs_price), int(qs_amount), str(qs_type) ))
        file_stream.close()
        print ("\nЗаписано в:", file)
    #списки для будущего анализа данных
    a = list() #ресурс
    b = list() #цена
    c = list() #количество
    d = list() #тип
    e = list() #приращение
    f = list() #баланс
    my_sum=0.
    my_sum_d=0.
    my_sum_r=0.
    increment=0.
    stream=0.
    print("\nСчитываем данные из файла и обрабатываем")
    r_stream = open(file, mode='r', encoding="utf-8")
    for line in r_stream.readlines():
        print ('\nline: ',line,end='')
        words = line.split(";")
        print ("words: ",words)
        a.append(words[0])
        b.append(float(words[1]))
        c.append(int(words[2]))
        d.append(words[3])

        if (words[3]=="Доходы"): increment=(float(words[1])*float(words[2]))
        if (words[3]=="Расходы"): increment=(-1*float(words[1])*float(words[2]))
        e.append(increment)
        stream+=increment
        f.append(stream)
        print (words[0], words[1], words[2], words[3], increment, stream)
        
        if (words[3]=="Доходы"): my_sum_d += float(words[1])*float(words[2])
        if (words[3]=="Расходы"): my_sum_r += float(words[1])*float(words[2])
    r_stream.close()
    
    print("\nконтрольная таблица списков")
    i=0
    for value in a:
        print(a[i], b[i], c[i], d[i], e[i], f[i])
        i=i+1
    
    
    print("\n\nmy_sum_d: ", my_sum_d)
    print("my_sum_r: ", my_sum_r)
    print("my_sum_d-my_sum_r: ", my_sum_d - my_sum_r)
       
    
    print ("\n\nСвойства списка c:")
    print("c: ",c)
    print ("type(c): ",type(c))
    print ("c__len__(): ", c.__len__())
    print ("c__sizeof__(): ", c.__sizeof__())
    print ("c.count: ", c.count('3.0'))
    print("sum(c): ", sum(c))
    print("max(c): ", max(c))
    print("min(c): ", min(c))
    c.sort()
    print("c.sort():",c)
    
    print ("\n\nСвойства списка a:")
    print("a: ",a)
    print ("type(a): ",type(a))
    print ("a__len__(): ", a.__len__())
    print ("a__sizeof__(): ", a.__sizeof__())
    a.sort()
    print("a.sort():",a)
    '''
    d=dict()
    d[a[0]]=1
    counter=1
    for i in range(1,a.__len__(),1):
        print(i, a[i])
        if (a[i-1]==a[i]): counter+=1
        else:
            d[a[i-1]]=counter
            counter=1
    d[a[i]]=counter
    print(d)
    d_list=list()
    for key in d.keys():
        d_list.append(key)
    print(d_list)
    d_list.sort()
    print(d_list)
    for item in d_list:
        print ("'",item,"':", d[item],",", sep='')
    '''
    print('''
</pre>
</body>
<html>
''')

