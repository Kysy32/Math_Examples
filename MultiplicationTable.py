from random import randint

from Exapmles import Examples


class MultiplicationTable(Examples):

    def __init__(self, secret_words, max_number):
        super().__init__(secret_words, max_number)
        self.examples = self.generate_examples()

    def generate_examples(self):
        temp = []
        for x in self.result:
            while True:
                first_number = randint(2, 10)
                second_number = randint(1,10)
                if first_number * second_number == x:
                    s = f'{first_number} * {second_number} = '
                    if s not in temp:
                        temp.append(s)
                    elif s in temp:
                        temp.append(f'{second_number} * {first_number} = ')
                    break
        return temp

