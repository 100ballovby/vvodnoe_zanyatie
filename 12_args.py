def say_hello(name):  # определение функции
    txt = f'Hello, {name}!'  # тело функции
    return txt  # возврат значения функции


# вызов функции
greet = say_hello('Andrew')  # функция возвращает результат работы в переменную
greet2 = say_hello('Julia')  # функция возвращает результат работы в переменную
print(greet)
print(greet2)
