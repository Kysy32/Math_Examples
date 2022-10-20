from pprint import pprint

from Addition import Addition
from Subtraction import Subtraction
from MultiplicationTable import MultiplicationTable

def introduction():
    print('')

def user_choice(text, max_number, operation):
    '''
    Take user inputs
    :param text:
    :param max_number:
    :param operation:
    :return:
    '''
    if max_number.isdigit():
        if operation == '-':
            user_choice = Subtraction(text, max_number)
            return user_choice
        elif operation == '+':
            user_choice = Addition(text, max_number)
            return user_choice
        elif operation == '*':
            user_choice = MultiplicationTable(text, max_number)
            return user_choice
        else:
            print('If you want to generate examples for addition you have to use + as a sign, for subtraction you have to use -')
            quit()
    else:
        print('Inputs must be: 1) word or sentence (use only characters of the alphabet) 2) number: integers 3) sign of the mathematical operation')
        quit()

def generate():

    introduction()
    text = input('Insert word or sentence which you want convert to morse code (use ony alphabet signs): ')
    operation = input('Insert the sign of the mathematical operation (+, -, * (multiplication table): ')
    max_number = input('Insert upper limit for generating examples (min 100): ')
    gen_examples = user_choice(text, max_number, operation)




    #test
    #print(gen_examples.result)
    #print(gen_examples.examples)
    print(gen_examples.morse_secret)
    pprint(gen_examples.CODE_DICT)


    for x in gen_examples.examples:
        print(x)

#run the script
if __name__ == "__main__":
    generate()

