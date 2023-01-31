# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 1 2 3 4 5 6 7  8  9 10 11   порядковые номера
# 0 1 1 2 3 5 8 13 21 34 55   числа Фибоначчи (следующее + предыдущее 1 + 0, 1 + 1, 2 + 1, 3 + 2 и т. д.)

# Пример: ввести число Фибоначчи 5 и вывести его порядковый номер (6) ,
# а если ввести число 6 , то выведется -1 , потому как в Фибоначчи нет числа 6

number = int(input())
fibonacci1 = 0 # первые два
fibonacci2 = 1 # числа Фибоначчи
i = 2 # счетчик с 2 , потому первые 2 числа уже даны (0 и 1)
while fibonacci2 <= number:     # 1 меньше или равно введенного числа в самом начале (соответствие числу Фибоначчи)
    if number == fibonacci2:      # если введенное число является числом Фибоначчи , то выведи его порядковый номер
        print(i)
        break
    fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2   # левая сторона принимающая , правая - отдающая
                                                                   # fibonacci1 получает значение fibonacci2 , 
                                                                   # а fibonacci2 получает значение fibonacci1 + fibonacci2
    i += 1
else:
    print(-1)


