def decrypt_cesar(text:str):
    for k in range(1, len(eng_alpha) + 1):
        text_ = ''
        for letter in secret_text:
            if letter in eng_alpha:
                text_ += eng_alpha[(eng_alpha.index(letter) - k) % len(eng_alpha)]
            else:
                text_ += letter
        print(text_)


secret_text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
eng_alpha = 'abcdefghijklmnopqrstuvwxyz'
decrypt_cesar(secret_text)
# Сдвиг k = 6 исходя из визуального определения текста