# Задача 35. Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым.
number = int(input('Введите число: '))
def prostor(n):
    for i in range(2, n):
        if n % i == 0:
            return ('yes')
        else:
            return ('no')
print(prostor(number))