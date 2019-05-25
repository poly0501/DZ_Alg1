Max1 = 0
Max2 = 0
print("Введите число")
X = int(input("X="))
while X != 0:
    while X % 10 != 0:
        Max2 += X % 10
        X=X//10
    if Max2 > Max1:
        Max1 = Max2
    Max2 = 0
    X = int(input("X="))
print("MAX =",Max1)