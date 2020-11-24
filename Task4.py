num_user = int(input('Введите целое число '))
current_max = 0
num = num_user

while num > 0:
    digit = num % 10
    if digit > current_max:
        current_max = digit
        if current_max == 9:
            break
    num = num // 10

print(f'Наибольшая цифра у введенного числа {num_user}: ', current_max)
