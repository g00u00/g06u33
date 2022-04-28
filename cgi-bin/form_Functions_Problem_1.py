# Задание 1(3)
# Имеется коробка со сторонами AхBхC (А – длина, В – ширина, С – высота).
# Определить, пройдёт ли она в дверной проём с размерами KхL (K – ширина, L – высота).

import sys

def problemSolver(arg1, arg2, arg3, arg4, arg5) :
    A = arg1
    B = arg2
    C = arg3
    K = arg4
    L = arg5
    if (A > 0) & (B > 0) & (C > 0) & (K > 0) & (L > 0) :
        if ((A < L) & (B < K)) | ((B < L) & (C < K)) | ((A < L) & (C < K)) :
            print('Yes')
        else :
            print('No')
    else :
        print('Invalid data!')

def formView() :
    print('''
<form action = './form_Problem_1.py' target = '_self' method = 'get'>
    Имя файла : <input type = 'Техт' name = 'file_name' value = 'g06u21_file.txt'>
    Режим открытия файла :
    <input type = 'radio' name = 'mode' value = 'a' checked> a - открытие на дозапись
    <input type = 'radio' name = 'mode' value = 'w'> w - открытие на запись
    A (int) : <input type = 'Техт' name = 'variable1' value = '1' tabindex = '1'>
    B (int) : <input type = 'Техт' name = 'variable2' value = '1' tabindex = '2'>
    C (int) : <input type = 'Техт' name = 'variable3' value = '1' tabindex = '3'>
    K (int) : <input type = 'Техт' name = 'variable4' value = '2' tabindex = '4'>
    L (int) : <input type = 'Техт' name = 'variable5' value = '2' tabindex = '5'>
    <input type = 'reset' name = 'reset' value = 'Reset'>
    <input type = 'submit' name = 'submit' value = 'Submit'>
</form>
    ''')

def fileWriting(form) :
    form_keys_list = list()
    for form_key in form.keys() :
        if ((form_key == 'variable1') or
            (form_key == 'variable2') or
            (form_key == 'variable3') or
            (form_key == 'variable4') or
            (form_key == 'variable5')) :
            form_keys_list.append(form_key)
    form_keys_list.sort()
    if 'file_name' in form :
        file = '../tmp/' + form['file_name'].value
        print('\nЗаписываем в:', file)
        if form['mode'].value == 'w' :
            # если файл не существует, создаём новый, в противном случае перезаписываем его
            file_stream = open(file, mode = 'w', encoding = 'utf-8', errors = None)
        elif form['mode'].value == 'a' :
            # если файл не существует, создаём новый, в противном случае дозаписываем в конец файла
            file_stream = open(file, mode = 'a', encoding = 'utf-8', errors = None)
        for form_key in form_keys_list :
            form_value = form.getvalue(form_key)
            # записываем данные в файл
            file_stream.write('%1s;%1s;' %(form_key, form_value))
            # выводим данные в консоль
            sys.stdout.write('%1s;%1s;' %(form_key, form_value))
        sys.stdout.write('\n')
        file_stream.write('\n')
        file_stream.close()

def fileReading(form) :
    if 'file_name' in form :
        file = '../tmp/' + form['file_name'].value
        file_stream = open(file, mode = 'r', encoding = 'utf-8')
        print('\nЧитаем строки из', file, 'и разбираем их на слова:')
        for line in file_stream.readlines() :
            word = line.split(';')
            print(word)
        file_stream.close()
