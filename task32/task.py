n=int(input("Введите количество элементов: "))
mas=list()
for i in range(n):
    a=int(input("Введите элемент: "))
    mas.append(a)
min=int(input("Введите наименьшее число: "))
max=int(input("Введите наибольшее число: "))
index=list()
for i in range(len(mas)):
    if (mas[i]>=min)&(mas[i]<=max):
        index.append(i)
        print(i ," ")
if len(index)<1:
    print("Нет таких элементов")