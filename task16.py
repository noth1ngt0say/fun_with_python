users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

print(f'Тип сортировки: \n'
      f'1 - По возрасту\n'
      f'2 - По первой букве логина\n'
      f'3 - По группе\n')
while True:
    lookup_criteria = int(input('Введите тип сортировки: '))
    if lookup_criteria in range(1, 4):
        break
    else:
        print("Не верный критерий поиска!")
while True:
    found = False
    match lookup_criteria:
        case 1:
            age = int(input('Введите критерий поиска: '))
            for user in users:
                if age < user['age']:
                    print(f"Пользователь: '{user['login']}' возраст {user['age']} года, группа \"{user['group']}\"")
                    found = True
            if not found:
                print("Нет пользователей удовлетворяющим критериям поиска.")
            break
        case 2:
            login_first_letter = input('Введите критерий поиска: ').lower()
            for user in users:
                if login_first_letter == user['login'][0].lower():
                    print(f"Пользователь: '{user['login']}' возраст {user['age']} года, группа \"{user['group']}\"")
                    found = True
            if not found:
                print("Нет пользователей удовлетворяющим критериям поиска.")
            break
        case 3:
            srch_group = input('Введите критерий поиска: ').lower()
            for user in users:
                if srch_group == user['group']:
                    print(f"Пользователь: '{user['login']}' возраст {user['age']} года, группа \"{user['group']}\"")
                    found = True
            if not found:
                print("Нет пользователей удовлетворяющим критериям поиска.")
            break


# Код выше показался каким то громозким и повторялись блоки

# def year_suffix(age):
#     if age % 10 == 1 and age % 100 != 11:
#         return "год"
#     elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
#         return "года"
#     else:
#         return "лет"
#
# def print_info(user):
#     suffix = year_suffix(user['age'])
#     print(f"Пользователь: '{user['login']}' возраст {user['age']} {suffix}, группа \"{user['group']}\"")
#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# print(f'Тип сортировки: \n'
#       f'1 - По возрасту\n'
#       f'2 - По первой букве логина\n'
#       f'3 - По группе\n')
#
# lookup_criteria = int(input('Введите тип сортировки: '))
#
# if lookup_criteria not in range(1, 4):
#     print("Неверный критерий поиска!")
# else:
#     match lookup_criteria:
#         case 1:
#             age = int(input('Введите возраст для поиска: '))
#             found = False
#             for user in users:
#                 if age < user['age']:
#                     print_info(user)
#                     found = True
#             if not found:
#                 print("Нет пользователей удовлетворяющим критериям поиска.")
#         case 2:
#             login_first_letter = input('Введите первую букву логина: ').lower()
#             found = False
#             for user in users:
#                 if login_first_letter == user['login'][0].lower():
#                     print_info(user)
#                     found = True
#             if not found:
#                 print("Нет пользователей удовлетворяющим критериям поиска.")
#         case 3:
#             srch_group = input('Введите группу для поиска: ').lower()
#             found = False
#             for user in users:
#                 if srch_group == user['group'].lower():
#                     print_info(user)
#                     found = True
#             if not found:
#                 print("Нет пользователей удовлетворяющим критериям поиска.")
