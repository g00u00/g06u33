import _NewTask_class
if __name__ == "__main__":
    formulation = "Формулировка задачи"
    dict_arguments = {'a':1, 'b':2, 'c':'3'}
    object_1 = _NewTask_class.NewTask(formulation, dict_arguments)
    result = object_1.processing()
    if (result == "Ошибка ввода"):
        print("Завершение. ", result)
    else:
        print(result)
        result = object_1.solution()
        print(result)




