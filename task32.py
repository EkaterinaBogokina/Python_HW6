# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)



massiv = [2, 9, 10, 6, 3, 66, 76, 23, 52, 93, 61, 3, 8, 4]
n_min=int(input("enter min number "))
n_max=int(input("enter max number "))

for i in range (len(massiv)):
        if n_min <= massiv[i] <=n_max:
            print(i)
