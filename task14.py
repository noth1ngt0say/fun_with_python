
#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = [1,2,17,54,30,89,2,1,6,2]
mass_len = len(mass)
index_lst = []
for key in range(mass_len):
    if mass.count(mass[key]) == 1:
        print(f'Для числа {mass[key]} нет минимального растояния т.к элемент в массиве один')
    dist = float('inf')
    for next_key in range(key + 1, mass_len):
        if mass[next_key] == mass[key] and mass.count(mass[key]) == 2:
            print(f'Для числа {mass[key]} минимальное растояние в массиве по индексам: {key} и {next_key}')
        elif mass[next_key] == mass[key] and mass.count(mass[key]) > 2:
            index_lst.append(next_key)
print(index_lst)
                # print(mass[key], next_key, key)