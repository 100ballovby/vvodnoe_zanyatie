a = 5
b = 3

print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False
print((a * 2) == (b * 3 + 1))  # равно (True)
print(a != b + 2)  # НЕ равно (False)

# ключевые слова is и in
x = 5
y = x

print(x is y)  # проверка того, что имена являются одним и тем же объектом
print(x == y)

family = 'семья'
print('я' in family)  # проверка того, что один объект находится внутри коллекции объектов
