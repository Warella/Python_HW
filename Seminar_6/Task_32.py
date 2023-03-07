# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)
import random
length = int(input('Введите длину массива: '))
lst = [random.randint(1, 10) for i in range(10)]
print(*lst)
max = 8
min = 5
for i in range (len(lst)):
    if min <= lst[i] <= max:
        print(i)