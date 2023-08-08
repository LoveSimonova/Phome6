a1=int(input("Введите первый элемент: "))
dn=int(input("Введите разницу: "))
d=int(input("Введите количество элементов: "))
list=list()
for i in range(d):
    k=a1+dn*i
    list.append(k)
for i in range(len(list)):
    print(list[i], " ")