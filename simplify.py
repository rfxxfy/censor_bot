import re

def simplify_word(word):
    word = re.sub(r'[\s\W\d]+', '', word)
    simplified_word = re.sub(r'(.)\1+', r'\1', word)
    return simplified_word