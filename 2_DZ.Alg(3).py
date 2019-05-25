print("Введите число")
X = int(input("X= "))
X2 = 0
while X > 0:
    X2 = X2*10 + (X % 10)
    X //= 10
print(X2)
