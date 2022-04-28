class NewTask:
    def __init__(self, formulation, dict_parameters):
        self.formulation = formulation
        self.dict_parameters =dict_parameters
        print(self.formulation , "\n", self.dict_parameters)

    def  processing(self):
        print("\n\nПроверка корректности ввода и корректировка данных")
        for key in self.dict_parameters:
            try:
                int_variable= int(self.dict_parameters[key])
                self.dict_parameters[key] = int_variable
            except Exception as identifier:
                print("\n\nОшибка в строке запроса, повторить ввод")
                print(identifier)
                return ("Ошибка ввода")
            else:
                pass
        print("\nИсходные данные откоректированы:")
        print(print (self.dict_parameters))
        return(self.dict_parameters)

    def solution(self):
        a = self.dict_parameters["a"]
        b = self.dict_parameters["b"]
        c = self.dict_parameters["c"]
        print(self.formulation)
        print(self.dict_parameters)
        if (a+b==c): print("a+b==c")
        else: print("a+b!=c")
        return()





