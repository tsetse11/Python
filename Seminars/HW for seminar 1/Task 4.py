# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Дольки по высоте: "))
m = int(input("Дольки по ширине: "))
k = int(input("Сколько хотите отломить: "))
if (k % n == 0 or k % m == 0) and n != 1 and m != 1 and k <= m * n:
    print("yes")
elif n == 1 and m == 1 and k == 1:
    print("yes")
else:
    print("no")