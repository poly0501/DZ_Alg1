from collections import namedtuple

TIME=4
Comp = namedtuple("Comp", "name, time, summa")
F = int(input('Введте количество компаний: '))
all_comp=set()
all_summa = 0
for i in range(F):
    summa = 0
    time = []
    name = input("name: ")
    for j in range(TIME):
        time.append(int(input(f"{j+1})")))
        summa+=time[j]
    comp = Comp(name =name,time=tuple(time),summa=summa)
    all_comp.add(comp)
    all_summa+=summa
    print(f"Общая прибыль", summa)
srednZN=all_summa / F
print(f"Средняя прибыль = ", srednZN)
print(f"\nКомпания с прибылью выше среднего:")
for comp in all_comp:
    if comp.summa>srednZN:
        print(f"Компания {comp.name} заработала {comp.summa}")

print(f"\nКомпания с прибылью ниже среднего:")
for comp in all_comp:
    if comp.summa<srednZN:
        print(f"Компания {comp.name} заработала {comp.summa}")