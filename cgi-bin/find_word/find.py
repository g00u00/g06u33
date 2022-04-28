# Галкина Ксения
# Задание 1 (19)
# Дано целое десятичное число.
# Переставить местами его крайние цифры при условии, что они нечётные.

import sys
import re

def problemSolver(arg1):
    print ('Пытаемся поменять местами первую и последнюю цифры в числе', arg1)
    if arg1 > 9:
        n_last = arg1 % 10
        if n_last % 2 == 1:
            p = 1
            while arg1 // (p * 10) > 0:
                p *= 10
            n_first = arg1 // p
            if n_first % 2 == 1:
                arg1 = (n_last * p) + (arg1 % p // 10 * 10) + n_first
                return arg1
            else:
                print('Первая цифра чётная!')
        else:
            print('Последняя цифра чётная!')
    else:
        print('Число не соответствует требованиям!')

def formView() :
    print('''
<form  action="./form_1_19.py"   target='_self' method='get'>
    Имя файла: <input type = 'Техт' name = 'file_name' value = 'g03u24_file.txt'>
    Режим открытия файла: 
    <input type = 'radio' name = 'mode' value = 'a' checked> a - открытие на дозапись
    <input type = 'radio' name = 'mode' value = 'w'> w - открытие на запись
    Введите число (int): <input type="Техт" name="variable1" value="12345" tabindex = '1'>
    Введите номер строки (int): <input type="Техт" name="n_line" value="1" tabindex = '2'>
    Введите букву (str): <input type="Техт" name="letter" value="д" tabindex = '3'>
    <input type="reset"  name="reset" value="Обновить">
    <input type="submit" name="submit" value="Отправить">
</form>
    ''')

def fileWriting(form, problem):
    keys_list = []
    for form_key in form.keys():
        if form_key == 'variable1' or form_key == 'n_line' or form_key == 'letter':
            keys_list.append(form_key)
    keys_list.sort()
    if 'file_name' in form :
        file = '../tmp/' + form['file_name'].value
        print('\nЗаписываем в:', file)
        if form['mode'].value == 'w':
            # если файл не существует, создаём новый, в противном случае перезаписываем его
            # так как начальном файле присутствует форумулировка проблемы, в случае перезаписи вновь добавляем её
            file_stream = open(file, mode='w', encoding='utf-8', errors=None)
            file_stream.write(problem +'\n')
            sys.stdout.write(problem + '\n')
        elif form['mode'].value == 'a':
            # если файл не существует, создаём новый, в противном случае дозаписываем в конец файла
            file_stream = open(file, mode='a', encoding='utf-8', errors=None)
        for form_key in keys_list:
            form_value = form.getvalue(form_key)
            # записываем данные в файл
            file_stream.write('%1s;%1s;' % (form_key, form_value))
            # выводим данные в консоль
            sys.stdout.write('%1s;%1s;' % (form_key, form_value))
        sys.stdout.write('\n')
        file_stream.write('\n')
        file_stream.close()

def fileReading(form):
    if 'file_name' in form :
        file = '../tmp/' + form['file_name'].value
        with open(file, mode = 'r', encoding = 'utf-8') as file_data:
            print('\n\nЧитаем строки с переменными из', file, 'и разбираем их на слова:')
            file_lines = file_data.readlines()
            # выводим значения, связанные непосредственно  с переменными
            for line in file_lines[1:]:
                if ';' in line:
                    word = line.split(';')
                    print(word)
    # возвращаем формулировку задания для дальнейшей обработки
    return file_lines[0]

def find_words(lines, n_line, letter):
    print('\n\nПытаемся дать ответ на задание по обработке строк.')
    # делим на строки по знаку "точка"
    problem_lines = re.findall('([\w\s,]*)\.', lines)
    if n_line == 1 or n_line == 2:
        # вычитаем 1, так как в списке нумерация от 0
        chosen_line = problem_lines[n_line - 1]
        # проверяем, подхоит ли нам введёная буква
        if len(letter) == 1 and letter.lower() in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя':
            # ищем отдельно слова как с заглавной, так и строчной буквы
            answer = []
            found_upper_word = []
            found_lower_word = []
            for word in chosen_line.split(' '):
                found_upper_word.extend(re.findall('^{}\w*'.format(letter.upper()), word))
                found_lower_word.extend(re.findall('^{}\w*'.format(letter.lower()), word))
            if found_upper_word:
                answer.extend(['В строке {} найдены слова, начинающиеся на прописную букву {}: '.format(n_line, letter.upper()) +
                               ', '.join(found_upper_word) + '. ' + 'Их количество: ' + str(len(found_upper_word))])
            else:
                answer.append('Слов, начинающихся с прописной заданной буквы, в заданной строке не найдено')
            if found_lower_word:
                answer.extend(['В строке {} найдены слова, начинающиеся на строчную букву {}: '.format(n_line, letter.lower()) +
                               ', '.join(found_lower_word) + '. ' + 'Их количество: ' + str(len(found_lower_word))])
            else:
                answer.append('Слов, начинающихся со строчной заданной буквы, в заданной строке не найдено')
            with open('../tmp/g03u24_file.txt', 'a', encoding = 'utf-8') as file:
                sys.stdout.write('\n'.join(answer) + '\n')
                file.write('\n'.join(answer) + '\n')
        else:
            print('Некорректный ввод буквы')
    else:
        print('Строка не существует')