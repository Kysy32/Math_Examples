from AdditionAndSubtraction import Addition, Subtraction
from fpdf import FPDF

def introduction():
    print('')

def user_choice(text, max_number, operation):
    if max_number.isdigit():
        if operation == '-':
            user_choice = Subtraction(text, max_number)
            return user_choice
        elif operation == '+':
            user_choice = Addition(text, max_number)
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
    max_number = input('Insert upper limit for generating examples: ')
    operation = input('Insert the sign of the mathematical operation: ')
    gen_examples = user_choice(text, max_number, operation)

    print(gen_examples.result)
    print(gen_examples.examples)

    for x in gen_examples.examples:
        print(x)


if __name__ == "__main__":
    generate()

