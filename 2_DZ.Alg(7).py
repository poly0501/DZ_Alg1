print("Проверим уравнение 1+2+...+n = n(n+1)/2 \nВведите n")
n = int(input("n="))
X1 = 0
i = 1
for i in range(n+1):
    X1 += i
X2 = n*(n+1)//2
print("Левая часть =", X1)
print("Правая часть =", X2)
if X1 == X2:
    print("Уравнение верное")
else:
    print("Уравнение НЕверное")
