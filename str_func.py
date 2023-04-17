'''Хорошая функция'''
def big_letter(string_: str):
    return string_.upper()


'''Функция меняет регистр первой буквы каждого словов строке'''


def big_first_letter(string_: str):
    result = []
    for word in string_.split(" "):
        result.append(word.title())
    return " ".join(result)
