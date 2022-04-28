def function_1(x, y):
    print("\nФункция выполняется")
    print(x, y)
    z = x + y
    print(x, y, z)
    return (z)


if __name__ == '__main__':
    print("Функция возвращает: ", function_1(1, 20))
