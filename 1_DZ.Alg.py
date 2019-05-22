# №3
print('Введите координаты точек M1 и M2')
print('M1:')
x1 = int(input('x1= '))
y1 = int(input('y1= '))
print('M2:')
x2 = int(input('x2= '))
y2 = int(input('y2= '))

k = int()
B = int()
if (x2 - x1) != 0:
    k = (y2 - y1) // (x2 - x1)
    B = y1 - k * x1
    if B > 0:
        print('Формула: %d*x + %d' % (k, B))
    else:
        print('Формула: %d*x %d' % (k, B))
else:
    print('Ошибка! Знаменатель равен 0!')

# №4
import random

print('С чем вы хотите работать?\nЦелый число - 1\nВещественное число - 2\nСимвол - 3')
Choice = int(input())

if Choice == 1:
    print('Введите ограничения целого числа')
    X1 = int(input('X1= '))
    X2 = int(input('X2= '))
    R = int()
    R = random.random() * (X2 - X1 + 1) + X1
    print('Число %d' % R)
if Choice == 2:
    print('Введите ограничения вищественного числа')
    X1 = float(input('X1= '))
    X2 = float(input('X2= '))
    R = float()
    R = random.random() * (X2 - X1) + X1
    print('Число %f' % R)
if Choice == 3:
    print('Введите ограничения символа')
    X1 = ord(input('X1= '))
    X2 = ord(input('X2= '))
    R = int(random.random() * (X2 - X1 + 1) + X1)
    # R = random.random() * (X2 - X1 + 1) + X1
    print(chr(R))

# №5
a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('Позиции: %d и %d' % (a, b))
print('Между буквами символов:', abs(a - b) - 1)

# №8
Year = int(input('Введте год: '))
if Year % 400 == 0 | (Year % 100 != 0 & Year % 4 == 0):
    print('%d год Високостный' % Year)
else:
    print('%d год Невисокостный' % Year)

    # №9
print('Введите 3 разны числа')
A = int(input())
B = int(input())
C = int(input())
if A < B:
    if C < A:
        print(A)
    else:
        if C > B:
            print(B)
        else:
            print(C)
else:
    if C < B:
        print(B)
    else:
        if C > A:
            print(A)
        else:
            print(C)