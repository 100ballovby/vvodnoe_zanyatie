x = 10  # задаю х значение 10
while True:  # бесконечный цикл
    print(x)  # вывожу значение х
    # x = x - 1
    x -= 1  # уменьшаю с присваиванием х на единицу
    if x <= 0:  # если х стал меньше/равен 0
        break  # прервать работу цикла