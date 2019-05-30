print("9)Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.")
Max1 = 0
Max2 = 0
N = int()
N2=0
print("Введите число")
X = int(input("X="))
N = X
while X != 0:
    N2=X
    while X % 10 != 0:
        Max2 += X % 10
        X = X//10
    if Max2 > Max1:
        N = N2
        Max1 = Max2
    Max2 = 0
    X = int(input("X="))
print("Число:", N)
print("MAX=", Max1)
