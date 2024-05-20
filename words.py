from pymystem3 import Mystem

mystem = Mystem()


def get_initial_form(word):
    lemmas = mystem.lemmatize(word)
    try:
        return lemmas[0].strip()
    except:
        return
