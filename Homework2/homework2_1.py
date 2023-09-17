# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите число монет: "))
orel = 0;
reshka = 0;

for i in range(n):
    var = (input("Введите O или Р: "))
    if var == "O":
        orel += 1
    else:
        reshka += 1

if orel >= reshka:
    print(f"Минимальное количество монет, которые нужно перевернуть = {reshka}")
elif reshka > orel: 
    print(f"Минимальное количество монет, которые нужно перевернуть = {orel}")
else:
    print("Минимальное количество монет, которые нужно перевернуть = 0")