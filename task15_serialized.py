import random
import os
import pickle

obj = {"penalty_score":None,
       "hidden_word":None,
       "hint":None,
       "field":None,
       "casino_save":None}

game_menu = """
    0. Выйти из игры
    1. Начать игру
    2. Загрузить игру
"""
print(game_menu)
menu_point = int(input('Что делаем дальше: '))

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования",
         "Это слово обозначает структурный элемент кода, который выполняет определённую задачу или набор действий в программе",
         "Это слово обозначает экземпляр класса с определенными значениями для его атрибутов"]
save_phrase = ['Только не "гугли"! Все ходы записаны!', 'Я тебя запомнил!', 'Я записал! Можешь подумать!']
exit_phrase = ['Ну ты это, заходи если что!', 'А я думал ты настроен серьёзно', 'Как говорил Illidan: You are not prepared!']
penalty_phrase = ['Ты проиграл! В следующий раз повезёт!', 'Не вешай нос! Попробуй ещё разок!', 'А как хорошо начиналось! Давай ещё!']

def init():
    penalty_score = 0
    word_index = random.randint(0, len(words) - 1)
    hidden_word = words[word_index]
    field = ['X'] * len(hidden_word)
    hint = desc_[word_index]
    print(hint, field, sep='\n')
    return penalty_score, hidden_word, field, hint


def game(penalty_score : int, hidden_word : str, field : list, hint: str):
    print('Чтобы сохранить игру введи "0" без кавычек!')
    while penalty_score < 10 and 'X' in field:
        letter = input('Введите букву: ')
        if letter in hidden_word:
            for key in range(len(hidden_word)):
                if letter == hidden_word[key]:
                    field[key] = letter
        elif letter == '0':
            casino_save = input('Решил сохраниться?! Отлично, как назовем?: ')
            obj["penalty_score"] = penalty_score
            obj["hidden_word"] = hidden_word
            obj["field"] = field
            obj["hint"] = hint
            obj["casino_save"] = casino_save
            with open(f'./savegame/asino777/{casino_save}.pkl', "wb") as fd:
                pickle.dump(obj, fd) # запись в файл
                print(save_phrase[random.randint(0, len(save_phrase) - 1)])
            exit(0)
        else:
            penalty_score += 1
            print(f'Нет такой буквы!\nУ вас осталось {10 - penalty_score} попыток!')
        print(field)
    if penalty_score == 10:
        print(penalty_phrase[random.randint(0, len(penalty_phrase) - 1)])
    else:
        print(f'Игра закончена! Поздравляю, Ты отгадал слово {hidden_word}!')
        exit(0)


match menu_point:
    case (1):
        start = init()
        game(start[0], start[1], start[2], start[3])
    case(2):
        dir = os.listdir('./savegame/asino777')
        for file in dir:
            print(file)
        casino_save = input('Выбери сохранение: ')
        with open(f'./savegame/asino777/{casino_save}', "rb") as fd:
            obj = pickle.load(fd)
        print(f'Игра {obj["casino_save"]} загружена успешна!')
        print(f'Подсказка\n{obj["hint"]}\n'
              f'{obj["field"]}\n'
              f'Количество попыток {10 - obj["penalty_score"]}')
        game(obj["penalty_score"], obj["hidden_word"], obj["field"], obj["hint"])
    case (0):
        print(exit_phrase[random.randint(0, len(exit_phrase) - 1)])