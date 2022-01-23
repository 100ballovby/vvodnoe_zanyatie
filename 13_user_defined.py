def power(num, p=2):
    """
    Функция возводит число num в степень p
    :param num: число
    :param p: степень
    :return: число num возведенное в степень p
    """
    res = 1
    for i in range(p):  # повторить p раз
        res *= num  # res = res * num
    return res


print(power(2, 9))
# Аргументы функции позиционные. Их нужно передавать в том порядке, в котором определены параметры
print(power(9, 2))
# Требование к позиционности пропадает при использовании именованных аргументов
print(power(p=9, num=2))
print(power(5))  # p=2
print(power(5, 7))  # p=7

