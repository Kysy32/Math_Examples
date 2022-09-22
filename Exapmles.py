from random import randint

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
        self.CODE_DICT = {'A': randint(1, int(max_number)), 'B': randint(1, 101),
                     'C': randint(1, int(max_number)), 'D': randint(1, int(max_number)), 'E': randint(1, int(max_number)),
                     'F': randint(1, int(max_number)), 'G': randint(1, int(max_number)), 'H': randint(1, int(max_number)),
                     'I': randint(1, int(max_number)), 'J': randint(1, int(max_number)), 'K': randint(1, int(max_number)),
                     'L': randint(1, int(max_number)), 'M': randint(1, int(max_number)), 'N': randint(1, int(max_number)),
                     'O': randint(1, int(max_number)), 'P': randint(1, int(max_number)), 'Q': randint(1, int(max_number)),
                     'R': randint(1, int(max_number)), 'S': randint(1, int(max_number)), 'T': randint(1, int(max_number)),
                     'U': randint(1, int(max_number)), 'V': randint(1, int(max_number)), 'W': randint(1, int(max_number)),
                     'X': randint(1, int(max_number)), 'Y': randint(1, int(max_number)), 'Z': randint(1, int(max_number))}
        self.result = self.results()

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
