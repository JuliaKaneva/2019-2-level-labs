"""
Labour work #3
 Building an own N-gram model
"""

from math import log
from random import randint
reference_text = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        reference_text = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        identifier = None
        if word not in self.storage and isinstance(word, str):
            while identifier not in self.storage.keys() and identifier is None:
                identifier = randint(1, 10000000)
            self.storage[word] = identifier
        return identifier

    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage.get(word)
        return -1

    def get_original_by(self, id: int) -> str:
        if id in self.storage.values() and isinstance(id, int):
            id = list(self.storage.values()).index(id)
            return list(self.storage.keys())[id]
        return 'UNK'

    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple):
            for word in corpus:
                self.put(word)
        return corpus


class NGramTrie:
    def __init__(self, n=2):
        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}
        self.prefixes = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if not isinstance(sentence, tuple) or len(sentence) < self.size:
            return 'error'
        ngramm = []
        for index, _ in enumerate(sentence[:-self.size + 1]):
            ngramm = []
            count = 0
            while count < self.size:
                ngramm.append(sentence[index + count])
                count += 1
            ngramm = tuple(ngramm)
            if ngramm in self.gram_frequencies:
                self.gram_frequencies[ngramm] += 1
            else:
                self.gram_frequencies[ngramm] = 1
        if ngramm == []:
            return 'error'
        return 'ok'

    def calculate_log_probabilities(self):
        for gramm in self.gram_frequencies:
            pref = gramm[:-1]
            if pref in self.prefixes:
                self.prefixes[pref] += self.gram_frequencies[gramm]
            else:
                self.prefixes[pref] = self.gram_frequencies[gramm]
        for gramm in self.gram_frequencies:
            if gramm in self.gram_log_probabilities:
                continue
            else:
                self.gram_log_probabilities[gramm] = log(self.gram_frequencies[gramm] /
                                                         self.prefixes[gramm[:-1]])

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple) or len(prefix) + 1 != self.size:
            return []
        sentence = list(prefix)
        while True:
            prob_list = []
            for gramm in list(self.gram_log_probabilities.keys()):
                if gramm[:-1] == prefix:
                    prob_list.append(self.gram_log_probabilities[gramm])
            if prob_list == []:
                break
            new_word = max(prob_list)
            for word, prob in list(self.gram_log_probabilities.items()):
                if new_word == prob:
                    new_word = word[-1]
            sentence.append(new_word)
            new_prefix = list(prefix[1:])
            new_prefix.append(new_word)
            prefix = tuple(new_prefix)
        return sentence


def encode(storage_instance, corpus) -> list:
    coded_text = []
    for sentence in corpus:
        coded = []
        for word in sentence:
            word = storage_instance.get_id_of(word)
            coded.append(word)
        coded_text.append(coded)
    return coded_text


def split_by_sentence(text) -> list:
    if text is None:
        return []
    if text == '':
        return []
    if '.' not in text:
        return []
    if not isinstance(text, str):
        text = str(text)
    text = text.lower()
    text = text.replace('\n', '')
    text = text.replace('  ', ' ')
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    new_text = ''
    splitted_sentences = []
    corpus = []
    for symbol in text:
        if symbol.isalpha() or symbol == ' ' or symbol == '.':
            new_text += symbol
    new_text = new_text.split('.')
    for sentence in new_text:
        sentence = sentence.split()
        splitted_sentences.append(sentence)
    for sentence in splitted_sentences:
        if len(sentence) != 0:
            new_line = ['<s>']
            for word in sentence:
                new_line.append(word)
            new_line.append('</s>')
            corpus.append(new_line)
    return corpus

def initialize():
    ref_txt = ''
    if __name__ == '__main__':
        with open('not_so_big_reference_text_1.txt', 'r') as example:
            ref_txt = example.read()
    ref_txt = split_by_sentence(ref_txt)
    print(str(len(ref_txt)) + " sentences in corpus")
    for sentence in ref_txt:
        for word in sentence:
            WS.put(word)
    print(str(len(WS.storage)) + " unique words")
    ref_txt = encode(WS, ref_txt)
    for sentence in ref_txt:
        NGR.fill_from_sentence(tuple(sentence))
    NGR.calculate_log_probabilities()


def prediction(words: str) -> list:
    final = []
    if not isinstance(words, str):
        return final
    test = []
    words = words.split()
    initialize()
    test.append(words)
    words = encode(WS, test)
    words = words[0]
    if len(words) != NGR.size - 1:
        return final
    for element in words:
        if element == -1:
            return final
    code = NGR.predict_next_sentence(tuple(words))
    for element in code:
        final.append(WS.get_original_by(element))
    return final


WS = WordStorage()
NGR = NGramTrie(2)
print(prediction('who'))


