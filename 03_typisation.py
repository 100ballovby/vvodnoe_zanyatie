a = 5  # тип данных int
b = 65.23  # тип данных float
c = 'five'  # тип данных str
x = '789'  # тип данных str
z = '5.34'  # тип данных str

# int(x), float(x), bool(x), str(x) <- функции для смены типа данных x
print(int(b))  # ✅
# print(int(c))  ❌
print(int(x))  # ✅
# print(int(z))  # ❌

print(float(a))  # ✅
# print(float(c))  ❌
print(float(x))  # ✅
print(float(z))  # ✅

print(int(float(z)))  # ✅

# в str можно превратить ЛЮБОЙ объект

print(bool(1))  # True
print(bool(0))  # False
print(bool(234))  # True
print(bool(-95))  # True

print(bool(''))  # False
print(bool([]))  # False
print(bool(' '))  # True
