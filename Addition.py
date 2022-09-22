from random import randint

from Exapmles import Examples


class Addition(Examples):

    def __init__(self, secret_words, max_number):
        super().__init__(secret_words, max_number)
        self.examples = self.generate_examples()

    def generate_examples(self):
        temp = []
        for x in self.result:
            first_number = randint(0, x)
            second_number = x - first_number
            temp.append(f'{first_number} + {second_number} = ')
        return temp