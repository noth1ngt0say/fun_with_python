red_letters = ['а', 'у', 'о', 'и', 'э',
               'ы', 'я', 'ю', 'е', 'ё']
f = open('dump.txt', 'r', encoding='utf-8')
text_ = f.read()
f.close()
for letter in red_letters:
    if letter in text_:
        count = text_.count(letter)
        print(f'Количество букв {letter} - {count}')
