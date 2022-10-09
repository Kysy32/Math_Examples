from random import shuffle
from MorseCode import MORSE_CODE_DICT

class Examples():

    def __init__(self, secret_words, max_number):
        self.secret_words =[x for x in secret_words.upper()]
        self.max_number = max_number
        self.morse_secret = self.secret()
        self.choices = self.choice()
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
    def secret(self):
        '''
        Converts input word/words to morse code
        '''
        temp = []
        for x in self.secret_words:
            if x in MORSE_CODE_DICT:
                temp.append(MORSE_CODE_DICT[x])
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

    def choice(self):
        choices = list(range(1, int(self.max_number) + 1))
        shuffle(choices)
        temp = []
        for x in choices:
            if x % 2 == 0 and x <= 20:
                temp.append(x)
            elif x % 3 == 0 and x <= 30:
                temp.append(x)
            elif x % 4 == 0 and x <= 40:
                temp.append(x)
            elif x % 5 == 0 and x <= 50:
                temp.append(x)
            elif x % 6 == 0 and x <= 60:
                temp.append(x)
            elif x % 7 == 0 and x <= 70:
                temp.append(x)
            elif x % 8 == 0 and x <= 80:
                temp.append(x)
            elif x % 9 == 0 and x <= 90:
                temp.append(x)

        return temp