def get_phrase(text : list):
    text_ = ''
    for hidden_letter in hidden_text:
        if hidden_letter.isdigit():
            hidden_letter = int(hidden_letter)
            if hidden_letter in range(1, len(eng_alpha) + 1):
                text_ += eng_alpha[hidden_letter - 1]
            if hidden_letter == 0:
                text_ += ' '
        else:
            text_ += hidden_letter

    return text_


hidden_text = [i for i in input().split()]
eng_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(get_phrase(hidden_text))

