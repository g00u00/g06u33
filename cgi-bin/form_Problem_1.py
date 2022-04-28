#!/usr/bin/env python3.4

import os, sys
import cgi, cgitb
import form_Functions_Problem_1

cgitb.enable()

print('''\
Content-type: text/html\r\n
<html>
<head>
<title>Problem 1(3)</title>
</head>
<body>
<pre>
''')

print('Задание 1(3)\n')
print('Имеется коробка со сторонами AхBхC (А – длина, В – ширина, С – высота).')
print('Определить, пройдёт ли она в дверной проём с размерами KхL (K – ширина, L – высота).')

form_Functions_Problem_1.formView()

form = cgi.FieldStorage()

if form :
    try :
        variable1 = int(form['variable1'].value)
        variable2 = int(form['variable2'].value)
        variable3 = int(form['variable3'].value)
        variable4 = int(form['variable4'].value)
        variable5 = int(form['variable5'].value)
    except Exception as message :
        print(message)
    else :
        form_Functions_Problem_1.problemSolver(variable1, variable2, variable3, variable4, variable5)
        form_Functions_Problem_1.fileWriting(form)
        form_Functions_Problem_1.fileReading(form)

print('''
</pre>
</body>
<html>
''')
