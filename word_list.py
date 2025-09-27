def make_list():
    set_words = []
    with open("words.txt") as text:
        for linea in text:
            word = linea.strip()
            if len(word) > 3 and len(word) < 9:
                set_words.append(word)
    return set_words

