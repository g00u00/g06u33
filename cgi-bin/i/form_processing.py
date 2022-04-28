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
    Цена: <input type="Text"  name="qs_price" value="0.00"    size=6 > 0 - очищаем файл
    Количество: <input type="Text"  name="qs_amount" value="0"    size=6 >
    Тип:<select name="qs_type">
        <OPTION value="Доходы">Доходы</OPTION> 
        <OPTION value="Расходы">Расходы</OPTION> 
        </select>
    <br><br><br>
    <input type="Hidden" name="file_name" value="qs_file.txt" >
    <input type="reset"  name="reset" value="Обновить">
    <input type="submit" name="submit" value="Отправить">
    </form>
    ''')
else:
    print ("\n\nНаименование:", form["qs_name"].value)
    print ("Цена:", form["qs_price"].value)
    print ("Количество:", form["qs_amount"].value)
    print ("Тип:", form["qs_type"].value)
    print ("\nЗаписываем в файл:", form["file_name"].value)
    file = "../tmp/"+form["file_name"].value
    if(form["qs_price"].value=='0'):#0 - очищаем файл 
        file_stream = open(file, mode='w', encoding="utf-8", errors=None)
        file_stream.close()
    file_stream = open(file, mode='a', encoding="utf-8", errors=None)
    file_stream.write("%2s;%3.2f;%1i;%1s;\n" % (str(form["qs_name"].value), float(form["qs_price"].value), int(form["qs_amount"].value), str(form["qs_type"].value) ))
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
        b.append(words[1])
        c.append(words[2])
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
    
    print("\nконтрольная таблица")
    i=0
    for value in a:
        print(a[i], b[i], c[i], d[i], e[i], f[i])
        i=i+1
    
    
    print("\n\nmy_sum_d: ", my_sum_d)
    print("my_sum_r: ", my_sum_r)
    print("my_sum_d-my_sum_r: ", my_sum_d - my_sum_r)
       
    
    print ("\n\nСвойства списка e:")
    print("e: ",e)
    print ("type(e): ",type(e))
    print ("e__len__(): ", e.__len__())
    print ("e__sizeof__(): ", e.__sizeof__())
    print ("e.count: ", e.count('3.0'))
    print("sum(e): ", sum(e))
    print("max(e): ", max(e))
    print("min(e): ", min(e))
    e.sort()
    print("e.sort():",e)
    
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
