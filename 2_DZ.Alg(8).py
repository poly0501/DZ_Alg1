print("Введите количество чисел")
N = int(input("N= "))
print("Введите цифру, которую мы будем искать")
z = int(input("z= "))
print("Введите %d чисел" % N)
c = 0
i = 0
for i in range(N):
    X = int(input((i+1)))
    while X!=0:
        if z == X % 10:
            c += 1
        X = X//10
print("Цифра %d встречается %d раз" % (z, c))


