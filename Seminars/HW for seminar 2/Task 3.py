# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

a = int(input())
n = 0
while a > 2**n:
    s = str(2**n)
