# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число > 0: "))
num = 1
k = 0

print(f"Целые степени двойки для числa {n}: ")
while num < n:
    print(num)
    num = 2**k 
    k += 1