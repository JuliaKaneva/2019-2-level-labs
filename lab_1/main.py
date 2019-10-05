"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""
text = """The quick, 6, brown fox jumps over the lazy dog!
The quick brown fox jumps over the lazy dog"""
stop_words = ['the', 'dog']


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

frequency = {
            'the': 2,
            'quick': 1,
            'brown': 3,
            'fox': 4,
            'jumps': 5,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }

def filter_stop_words(frequency, stop_words):

    if frequency is None or stop_words is None:
        return {}
    if frequency is None and stop_words is None:
        return {}
    if not stop_words:
        return frequency
    if not frequency:
        return {}
    if frequency == frequency:
        return  frequency

    for k in stop_words:
        if k in frequency:
            del(frequency[k])
    return frequency

top_n = 5
def get_top_n(frequency, top_n):
    def by_value(item):
        return item[1]

    frequency_list = list(frequency.items())
    res = sorted(frequency_list, key=by_value, reverse=True)
    top_n_words = res[:top_n]
    print (top_n_words)


get_top_n(frequency, top_n)
