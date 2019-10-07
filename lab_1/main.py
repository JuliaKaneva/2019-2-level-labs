"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text):
    if text is None or isinstance(text, int):
        return {}
    text = text.lower()
    res = ''
    for i in range(len(text)):
        if text[i].isalpha() or text[i] == ' ':
            res += text[i]
        elif text[i] == '\n':
            res += ' '
    res = res.split()

    frequency = {}
    for word in res:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    return frequency


def filter_stop_words(frequency, stop_words):

    if frequency is None or stop_words is None:
        return {}
    if frequency is None and stop_words is None:
        return {}
    if not stop_words:
        return frequency
    if not frequency:
        return {}
    list_of_keys = list(frequency.keys())

    for k in list_of_keys:
        if isinstance(k, int):
            del(frequency[k])

    for word in stop_words:
        if word in frequency:
            del(frequency[word])
    return frequency


def get_top_n(frequency, top_n):

    if frequency is None:
        return ()
    if top_n < 0 or top_n == 0:
        return ()

    if top_n > len(frequency) or top_n == len(frequency):
        keys = frequency.keys()
        return tuple(keys)

    else:
        list_of_keys = list(frequency.keys())
        top_n_words = list_of_keys[:top_n]
        top_n_words = tuple(top_n_words)
        return top_n_words


