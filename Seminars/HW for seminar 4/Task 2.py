# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, укаждого куста 
# есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают 
# разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import random

list = [random.randint(1, 10) for _ in range(int(input()))]

print(f'Максимальное число ягод, которое может собрать за один заход собирающий модуль: {max([sum([list[i -1], list[i], list[i + 1]]) if i != len(list) - 1 else sum([list[i - 1], list[i], list[0]]) for i in range(len(list))])}')