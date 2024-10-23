def text_crypting():
    crypted_text = ''
    text_ = []
    f = open('message.txt', 'r', encoding='utf8')
    line = f.readline()
    while line:
        text_.append(line.strip())
        line = f.readline()
    f.close()

    for num_line in range(len(text_)):
        move = num_line + 1
        for letter in text_[num_line]:
            if 'а' <= letter <= 'я':
                crypted_letter = chr((ord(letter) - ord('а') + move) % 32 + ord('а'))
            elif 'А' <= letter <= 'Я':
                crypted_letter = chr((ord(letter) - ord('А') + move) % 32 + ord('А'))
            else:
                crypted_letter = letter
            crypted_text += crypted_letter
        crypted_text += '\n'
    return crypted_text


def create_new_message():
    f = open('crypted_message.txt', 'w', encoding='utf8')
    f.write(text_crypting())
    f.close()


create_new_message()
print(text_crypting())

