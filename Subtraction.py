from random import randint

from Exapmles import Examples


class Subtraction(Examples):

    def __init__(self, secret_words, max_number):
        super().__init__(secret_words, max_number)
        self.examples = self.generate_examples()

    def generate_examples(self):
        temp = []
        for x in self.result:
            first_number = randint(1, x)
            second_number = x + first_number
            if second_number != 0:
                temp.append(f'{second_number} - {first_number} = ')
        return temp
