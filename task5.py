#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

# Не уточнён порядок чисел, принимаю что все действия производят с первым числом

print("Введите два числа: ")
dig_one, dig_two = int(input("Первое число: ")), int(input("Второе число: "))
summ = dig_one + dig_two
dif = dig_one - dig_two
div = dig_one / dig_two
mult = dig_one * dig_two
integer_div = dig_one // dig_two
div_rem = dig_one % dig_two
deg = dig_one ** dig_two

print(f'Сумма чисел: {summ}\n'
      f'Разность чисел: {dif}\n'
      f'Частное: {div}\n'
      f'Произведение чисел: {mult}\n'
      f'Челочисленное деление чисел: {integer_div}\n'
      f'Деление с остатком: {div_rem}\n'
      f'Возведение в степень:{deg}\n')