print("Введите количество элементов")
N = int(input("N= "))
c = 1
print("Все элементы:")
print(c)
for i in range(N-1):
    c = c * (-0.5)
    print(c)
print("\nОтвет:")
print(c)
