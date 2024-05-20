def translit_to_cyrillic(text):
    translit_dict = {
        'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'yo': 'ё', 'zh': 'ж', 'z': 'з',
        'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р',
        's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'h': 'х', 'c': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ',
        'y': 'ы', 'yu': 'ю', 'ya': 'я', 'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д', 'E': 'Е',
        'Yo': 'Ё', 'Zh': 'Ж', 'Z': 'З', 'I': 'И', 'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н',
        'O': 'О', 'P': 'П', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У', 'F': 'Ф', 'H': 'Х', 'C': 'Ц',
        'Ch': 'Ч', 'Sh': 'Ш', 'Shch': 'Щ', 'Y': 'Ы', 'Yu': 'Ю', 'Ya': 'Я'
    }

    for key in ['shch', 'Shch', 'zh', 'Zh', 'ch', 'Ch', 'sh', 'Sh', 'yo', 'Yo', 'yu', 'Yu', 'ya', 'Ya']:
        text = text.replace(key, translit_dict[key])
        del translit_dict[key]

    for key in translit_dict:
        text = text.replace(key, translit_dict[key])

    return text