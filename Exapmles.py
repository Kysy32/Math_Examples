from random import shuffle

class Examples():
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..'}

    def __init__(self, secret_words, max_number):
        self.secret_words =[x for x in secret_words.upper()]
        self.morse_secret = self.secret()
        self.choices = list(range(1, int(max_number) + 1))
        self.shuffles()
        self.CODE_DICT = {'A': self.choices.pop(), 'B': self.choices.pop(),
                          'C': self.choices.pop(), 'D': self.choices.pop(),
                          'E': self.choices.pop(),
                          'F': self.choices.pop(), 'G': self.choices.pop(),
                          'H': self.choices.pop(),
                          'I': self.choices.pop(), 'J': self.choices.pop(),
                          'K': self.choices.pop(),
                          'L': self.choices.pop(), 'M': self.choices.pop(),
                          'N': self.choices.pop(),
                          'O': self.choices.pop(), 'P': self.choices.pop(),
                          'Q': self.choices.pop(),
                          'R': self.choices.pop(), 'S': self.choices.pop(),
                          'T': self.choices.pop(),
                          'U': self.choices.pop(), 'V': self.choices.pop(),
                          'W': self.choices.pop(),
                          'X': self.choices.pop(), 'Y': self.choices.pop(),
                          'Z': self.choices.pop()}
        self.result = self.results()

    def shuffles(self):
        temp = (shuffle(self.choices))
        return temp

    def secret(self):
        '''
        Converts input word/words to morse code
        '''
        temp = []
        for x in self.secret_words:
            if x in Examples.MORSE_CODE_DICT:
                temp.append(Examples.MORSE_CODE_DICT[x])
            elif x == ' ':
                temp.append(x)
        return ' '.join(temp)

    def results(self):
        '''
        Produces a list of results for each letter of the given word
        '''
        temp = []
        for x in self.secret_words:
            if x in self.CODE_DICT:
                temp.append(self.CODE_DICT[x])
            elif x == ' ':
                continue
        return temp