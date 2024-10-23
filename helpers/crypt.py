def text_crypting(move: int):
    crypted_text = ''
    f = open('message.txt', 'r', encoding='utf8')
    text_ = f.readlines()
    f.close()

    for num_line in range(len(text_)):
        for letter in text_[num_line]:
            if 'а' <= letter <= 'я':
                crypted_letter = chr((ord(letter) - ord('а') + move) % 32 + ord('а'))
            elif 'А' <= letter <= 'Я':
                crypted_letter = chr((ord(letter) - ord('А') + move) % 32 + ord('А'))
            else:
                crypted_letter = letter
            crypted_text += crypted_letter
        # crypted_text += '\n'
    print('text_crypting')
    return crypted_text


def create_new_message(move: int):
    f = open('crypted_message.txt', 'w', encoding='utf8')
    f.write(text_crypting(move))
    f.close()
    print('create_new_message')

