import requests
from bs4 import BeautifulSoup
import re
import words, simplify, cyrillic, scripts

cache = {}


def request(word):
    if word in cache:
        return cache[word]
    url = f"https://ru.wiktionary.org/wiki/{word}"
    response = requests.get(url)
    cache[word] = response
    return response

def is_word_obscene(word):
    word = cyrillic.translit_to_cyrillic(word).lower()
    if word in scripts.OBSCENE_WORDS or 'залуп' in word:
        return True
    word = words.get_initial_form(simplify.simplify_word(word))
    response = request(word)

    if response.status_code != 200:
        for elem in scripts.DATA:
            if elem in word:
                return True
        return False

    soup = BeautifulSoup(response.content, 'html.parser')
    new_text = []

    for elem in soup.text.split("\n"):
        if elem == "Синонимы":
            break
        else:
            if elem != "":
                new_text.append(elem)

    new_text = "\n".join(new_text)

    pattern = r'([^.]*?обсц[^.]*\.)'
    matches = re.findall(pattern, new_text, re.IGNORECASE)


    return bool(matches)

