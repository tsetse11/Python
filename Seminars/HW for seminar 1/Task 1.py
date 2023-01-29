# Найдите сумму цифр трехзначного числа.

number = int(input("Введите трёхзначное число: \n"))
sum = 0
while number > 0:
    n = number % 10
    sum += n
    number = number // 10
print(f"Сумма цифр равна {sum}")