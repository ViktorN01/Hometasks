num = int(input('Введите целое положительное число:  '))
big_digit = 0
num1 = num

while  num1 > 0:
    digit = num1 % 10
    if digit > big_digit:
        big_digit = digit
        if big_digit == 9:
            break
    num1 = num1 // 10
print(f'Наибольшая цифра в числе {num} равна {big_digit}')
