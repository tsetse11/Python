# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите количество элементов массива: "))
list = [int(input()) for _ in range(n)]
number = int(input("Число: "))
list.append(number)
list.sort()
if number != max(list):
    index_number = list.index(number)
    if list[index_number] - list[index_number - 1] > list[index_number + 1] - list[index_number]:
        print(f"Близким по величине элемент к числу {number} является {list[index_number + 1]}")
    elif list[index_number] - list[index_number - 1] == list[index_number + 1] - list[index_number]:
        print(f"Близким по величине элемент к числу {number} является {min(list[index_number + 1], list[index_number - 1])}")
    else:
         print(f"Близким по величине элемент к числу {number} является {list[index_number - 1]}")

else:
    print(f"Близким по величине элемент к числу {number} является {list[len(list)-2]}")