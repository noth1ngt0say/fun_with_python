import random

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования",
         "Это слово обозначает структурный элемент кода, который выполняет определённую задачу или набор действий в программе",
         "Это слово обозначает экземпляр класса с определенными значениями для его атрибутов"]
penalty_score = 0
word_index = random.randint(0, len(words) - 1)
hidden_word = words[word_index]
field = ['X'] * len(hidden_word)
hint = desc_[word_index]
print(hint, field, sep='\n')
while penalty_score < 10 and 'X' in field:
    letter = input('Введите букву: ')
    if letter in hidden_word:
        for key in range(len(hidden_word)):
            if letter == hidden_word[key]:
                field[key] = letter
    else:
        penalty_score += 1
        print(f'Нет такой буквы!\nУ вас осталось {10 - penalty_score} попыток!')
    print(field)
if penalty_score == 10:
    print("У вас закончились попытки, Вы проиграли!")
else:
    print(f'Игра закончена! Поздравляю, Вы отгадали слово {hidden_word}!')