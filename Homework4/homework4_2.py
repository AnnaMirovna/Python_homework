# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов: "))
list_berries = []

for i in range(n):
    list_berries.append(int(input(f"Введите число ягод для {i+1} куста : ")))

count_berries = []
for i in range(len(list_berries)-1):
    count_berries.append(list_berries[i-1] + list_berries[i] + list_berries[i+1])
# count_berries.append(list_berries[-2] + list_berries[-1] + list_berries[0])

print(max(count_berries))

