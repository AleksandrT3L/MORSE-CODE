from eng_list import MORSE_CODE_DICT_ENG

def encode(text):
    text_list = [letter.title() for letter in text]
    list_morse = [MORSE_CODE_DICT_ENG[letter] for letter in text_list]
    return " ".join(list_morse)

#Декодирование
def decode(list_morse):
    text_list = []
    for word in list_morse:
        for letter in word.split():
            try:
                if text_list[-2] == "?" or text_list[-2] == "." or text_list[-2] == "!":
                    for i in MORSE_CODE_DICT_ENG:
                        if letter == MORSE_CODE_DICT_ENG[i]:
                            text_list.append(i.upper())
                else:
                    for i in MORSE_CODE_DICT_ENG:
                        if letter == MORSE_CODE_DICT_ENG[i]:
                            text_list.append(i.lower())
            except IndexError:
                for i in MORSE_CODE_DICT_ENG:
                    if letter == MORSE_CODE_DICT_ENG[i]:
                        text_list.append(i.lower())
        # Пробел между словами и первая буква заглавная
        text_list.append(" ")
        text_list[0] = text_list[0].upper()
    # Удаление лишнего пробела
    del text_list[-1]
    return "".join(text_list)