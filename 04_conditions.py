'''Синтаксис условий
if высказывание:
--->тело_условия
elif высказывание_2:
--->тело_условия_2
else:
--->дефолтное_тело
'''
import random

x = random.randint(1, 100)  # random_integer(a, b) <- возвращает число в промежутке от a до b (включительно)
if x % 2 == 0:
    print(x, 'четное')
else:
    print(x, 'нечетное')

# проверить число на делимость на 3 и на 5
if (x % 3 == 0) and (x % 5 == 0):  # если х делится на 3 И делится на 5 без остатка
    print(x, 'делится на 3 и на 5')
elif (x % 3 == 0) and not(x % 5 == 0):  # если х делится на 3 И НЕ делится на 5 без остатка
    print(x, 'делится только на 3')
elif not(x % 3 == 0) and (x % 5 == 0):  # если х НЕ делится на 3 И делится на 5 без остатка
    print(x, 'делится только на 5')
else:
    print(x, 'не делится ни на 3, ни на 5')

