import os,sys
import json

def form_dictionary(form):
    print ("Анализ строки запроса")
    print ("ключи(form.keys):",form.keys())
    form_keys_list=list()
    form_values_list=list() 
    form_dict=dict() 
    print  ("Названия ключей  и их значения (как есть)")
    i=0
    for form_key in form.keys():
        print  (i,  ": ", form_key," = ", form.getvalue(form_key))
        form_keys_list.append(form_key)
        form_values_list.append(form.getvalue(form_key))
        form_dict.update({form_key: form.getvalue(form_key)})
        i+=1
    
    print('\nВ виде словаря (form_dict):\n', form_dict)

    # сортируем список ключей (что-бы поля не сбоили при выводе в файл)
    print  ("\n\n","Ключи  и их значения после сортировки ")
    form_keys_list.sort()
    i=0
    for form_key in form_keys_list:
        print  (i,  ": ", form_key," = ", form.getvalue(form_key))
        i+=1
    print("form_keys_list: ", form_keys_list)
    
    if "experience" in form:
        print('\n\n Пример списка из строки запроса (experience): ', form.getvalue('experience'))
        strExperiences = form.getvalue('experience')
        print("strExperiences: ", strExperiences)
        intExperiences = list()
        for item in strExperiences: intExperiences.append(int(item))
        print("intExperiences: ", intExperiences, "   sum(intExperiences): ", sum(intExperiences), "\n")
    print('\n\nАнализируем и решаем  задачу')
    print("\nФормулировка  задачи:\n",
        "Ввести переменную один, переменую два и переменную три.",
        "Равна ли переменная три сумме переменных один и два",sep='')

    print("\n\nПроверка правильности ввода")
    try:
        variable_1 = int(form.getvalue('variable_1'))
        variable_2 = int(form.getvalue('variable_2'))
        variable_3 = int(form.getvalue('variable_3'))
    except Exception as identifier:
        print("\n\nОшибка в строке запроса, повторить ввод")
        print(identifier)
    else:
        print("Исходные данные:")
        print("Переменная один = ", variable_1)
        print("Переменная два = ", variable_2)
        print("Переменная три = ", variable_3)
        print("\n\nРезультаты  решения задачи:")
        if(variable_1 + variable_2 == variable_3):
            print ("Переменая три равна сумме переменных один и два")
        else:
            print ("Переменая три не равна сумме переменных один и два")
    return (form_dict)


def print_form_file(form):
    print("\n\nФормулируем очередную задачу и задаем переменные:\n",
        "Ввести переменную один, переменую два и переменную три.",
        "Равна ли переменная три сумме переменных один и два",sep='')
    print('<form  action="./form_action_file.py" target="_self" method="get">')
    #print('<form  action="./py_sql_pages.py" target="_self" method="get">')
    print('''
Переменная один:<input type="Техт" name="variable_1" value="1" >
Переменная два:<input type="Техт" name="variable_2" value="2" >
Переменная три:<input type="Техт" name="variable_3" value="3" >
experience: <input type="number" name="experience" value="11">
experience: <input type="number" name="experience" value="22">

<!--Нижерасположенное удалять нельзя, редактировать можно-->
Название файла: <input type="Техт" name="000_file_name" value="g06u33_file.txt" >
Тип записи в файл:<select name="010_mode">
<OPTION value="a">a - дозаписать в файл(таблицу базы)</OPTION> 
    <OPTION value="w">w - очистить файл(таблицу базы) и записать </OPTION> 
    </select>
<input type="hidden" name="015_abc" value="5">    
<input type="hidden" name="function" value="page">
<input type="hidden" name="page_id" value="8">
<input type="submit" name="submit" value="Отправить">
    ''')
    print("</form>")

def file_list(form):
    form_keys_list=list()
    for form_key in form.keys():
        if (form_key == "variable_1" or form_key == "variable_2" or form_key == "variable_3"):
            form_keys_list.append(form_key)
    form_keys_list.sort()
    if "000_file_name" in form:
        file = "../tmp/" + form["000_file_name"].value
        print ("\nЗаписываем в:", file)
        if(form["010_mode"].value=='w'):#0 - очищаем файл 
            file_stream = open(file, mode='w', encoding="utf-8", errors=None)
            file_stream.close()
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)
        for form_key in form_keys_list:
            form_value = form.getvalue(form_key)
            file_stream.write("%1s;%1s;" % (form_key, form_value ))
            sys.stdout.write("%1s;%1s;" % (form_key, form_value ))
        file_stream.write("\n")
        file_stream.close()

        listB = list() #для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print ("\n\nПострочно считываем строки из ", file, "и разбираем на слова\n")
        for line in r_stream.readlines():
            words = line.split(";")
            print(words)
            listB.append(int(words[5]))
        print("\nlistB(Список из столбца с ключом variable_3):", listB)
        print("listB.__len__():", listB.__len__())

def file_list_bash(form):
    form_keys_list=list()
    for form_key in form.keys():
        if (form_key == "ls" or form_key == "mkdir_mv_rm_cp"):
            form_keys_list.append(form_key)
    form_keys_list.sort()
    if "000_file_name" in form:
        file = "../tmp/" + form["000_file_name"].value
        print ("\nЗаписываем в:", file)
        if(form["010_mode"].value=='w'):#0 - очищаем файл 
            file_stream = open(file, mode='w', encoding="utf-8", errors=None)
            file_stream.close()
        file_stream = open(file, mode='a', encoding="utf-8", errors=None)
        for form_key in form_keys_list:
            form_value = form.getvalue(form_key)
            file_stream.write("%1s;%1s;" % (form_key, form_value ))
            sys.stdout.write("%1s;%1s;" % (form_key, form_value ))
        file_stream.write("\n")
        file_stream.close()

        listB = list() #для формирования списка из столбца файла
        r_stream = open(file, mode='r', encoding="utf-8")
        print ("\n\nПострочно считываем строки из ", file, "и разбираем на слова\n")
        for line in r_stream.readlines():
            words = line.split(";")
            print(words)
            listB.append(int(words[1]))
        print("\nlistB(Список из столбца с ключом ....):", listB)
        print("listB.__len__():", listB.__len__())