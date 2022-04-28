def task():
    print("\nФормулировка  задачи:",
        "\nВвести переменную один, переменую два и переменную три.",
        "\nРавна ли переменная три сумме переменных один и два?",sep='')
    print("\n\nВвод и проверка правильности ввода")
    try:
        variable_1 = int(input('Введите переменную 1: '))
        variable_2 = int(input('Введите переменную 2: '))
        variable_3 = int(input('Введите переменную 3: '))
    except Exception as identifier:
        print("\n\nОшибка в строке ввода, повторить ввод")
        print(identifier)
    else:
        print("\nИсходные данные:")
        print("Переменная один = ", variable_1)
        print("Переменная два = ", variable_2)
        print("Переменная три = ", variable_3)
        print("\nРезультаты  решения задачи:")
        if(variable_1 + variable_2 == variable_3):
            print ("Переменая три равна сумме переменных один и два")
        else:
            print ("Переменая три не равна сумме переменных один и два")
    return ()
1

if __name__=='__main__':
    task()