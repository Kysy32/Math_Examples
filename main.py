from random import randint

from pprint import pprint

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

class Subtraction(Examples):

    def __init__(self, secret_words, max_number, mathematical_operation):
        super().__init__(secret_words, max_number)
        self.mathematical_operation = mathematical_operation
        self.examples = self.generate_examples()

    def generate_examples(self):
        temp = []
        for x in self.result:
            first_number = randint(0, x)
            second_number = x + first_number
            temp.append(f'{second_number} - {first_number} = ')
        return temp

class Addition(Examples):

    def __init__(self, secret_words, max_number, mathematical_operation):
        super().__init__(secret_words, max_number)
        self.mathematical_operation = mathematical_operation
        self.examples = self.generate_examples()

    def generate_examples(self):
        temp = []
        for x in self.result:
            first_number = randint(0, x)
            second_number = x - first_number
            temp.append(f'{first_number} + {second_number} = ')
        return temp


class Multiplication(Examples):

    def __init__(self, secret_words, max_number, mathematical_operation):
        super().__init__(secret_words, max_number)
        self.mathematical_operation = mathematical_operation

class Division(Examples):

    def __init__(self, secret_words, max_number, mathematical_operation):
        super().__init__(secret_words, max_number)
        self.mathematical_operation = mathematical_operation

class Mix(Examples):

    def __init__(self, secret_words, max_number, mathematical_operation):
        super().__init__(secret_words, max_number)
        self.mathematical_operation = mathematical_operation

#test = Examples('Skakal pes',100)

#print(test.result)
#pprint(test.CODE_DICT)
#print(test.result)


kus = Subtraction('asas', 100, '-')

print(kus.result)
print(kus.morse_secret)

print(kus.examples)