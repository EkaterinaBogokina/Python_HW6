# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a=int(input("enter number "))
n=int(input("enter number of items "))
d=int(input("enter difference of numbers "))
arithm_progression = []
for i in range(n):
    i=a+i*d
    arithm_progression.append(i)
    print(arithm_progression)

