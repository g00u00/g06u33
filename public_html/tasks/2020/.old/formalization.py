#!/usr/bin/env python3.4
#wget http://ed.nn2000.info/public_html/050_python/tasks/formalization.py
import cgi, cgitb
#import developer_file #импортируем  developer_file.py
#import lr1_file #импортируем lr1_file.py
#cgitb.enable() #при поиске ошибок через браузер эту строку раскомментировать


def developer(): #о разработчике
    import os, sys, datetime
    print("Исполнитель, место и время исполнения")
#ssh
    #print(os.environ['USER'])  #ssh
    #print(os.environ['PWD']) #ssh
#http при отладке с SSH 3 строки ниже закомментировать 
    print("Сайт: ",os.environ['HTTP_HOST']) #http
    print("Раздел на сервере: ", os.environ['CONTEXT_DOCUMENT_ROOT']) #http
    print("IP клиента: ", os.environ['REMOTE_ADDR']) #http

    print("Дата и время исполнения программы: ", datetime.datetime.today().strftime('%Y-%m-%d %H:%M'))


def lr1(form): #пример лабораторной
    '''
    print (type(form))
    print ("form.keys:",form.keys())
    i=0
    for key in form.keys():
        variable = str(key)
        value = str(form.getvalue(variable))
        print  (str(i) +  ":  " + variable +" = "+ value)
        i+=1
    '''
    
    if "last_name" in form:
        print ("\nБыло введено...")
        print ("Фамилия: ", form["last_name"].value)
        print ("Год рождения: ", form["year_of_birth"].value)
        print ("Опыт работы: ", form["experience"].value)
    
    
    print(\
    '\n<form  action="formalization.py"   target="_self" method="get">',
    '\nВведите ...',
    '\nФамилия: <input type="Text" name="last_name" value=""   size=8 >',
    '\nГод рождения: <input type="Text" name="year_of_birth" value=""  size=8>',
    '\nОпыт работы: <input type="Text" name="experience" value="" size=8>',
    '\n<input type="Submit" name="Submit" value="Отправить данные на сервер">'
    )
    

print('''\
Content-type:text/html\r\n
<!DOCTYPE html>
<html>
<head>\n<title>Лабораторная работа</title>\n</head>
<body>
<pre>
''')

#О разработчике
#developer_file.developer()
developer()

#Оформление лабораторной
print("\nФормулировка задачи(источник, страница, номер задачи , текст задачи)")
print('''\
...
''')

print("\n\nСодержание файла считываемых данных")
print('''\
...
''')

print("\n\nРешение лабораторной")
form = cgi.FieldStorage()
#lr1_file.lr1(form)
lr1(form)

print("\n\nСодержание файла с результатами")
print('''\
...
''')
print("\n</pre>")
print("</body>")
print("</html>")

