#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

# lst = [_ for _ in range(10)]
# new_lst = []
# for index, value in enumerate(lst):
#     new_lst.append(value + 1)
# print(new_lst)

lst = [_ for _ in range(10)]
new_lst = []
for num in range(len(lst)):
    new_lst.append(lst[num] + 1)
print(new_lst)