# Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input("Введите номер билета: \n"))
sum1 = 0
sum2 = 0
for i in range(6):
    while number > 0:
        if number > 1000:
            n = number % 10
            sum1 += n
            number = number // 10
        else:
            n = number % 10
            sum2 += n
            number = number // 10
if sum1 == sum2:
    print("Билет счастливый")
else:
    print("Не повезло")