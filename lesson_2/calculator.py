# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Perform the operation on the two numbers.
# Print the result to the terminal.

import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the JSON file
json_file_path = os.path.join(script_dir, 'calculator_messages.json')

with open(json_file_path, 'r') as file:
    MESSAGES = json.load(file)

# Rest of your code...

def messages(message, language):
    return MESSAGES[language][message]

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

#Set a default language
language = 'EN'

want_to_calculate = True
while want_to_calculate:
    prompt(messages('welcome',language))
    # Ask the user for the first number.
    prompt("What's the first number?")
    num1 = input()

    while invalid_number(num1):
        prompt(messages('invalid_number', language))
        num1 = input()

    # Ask the user for the second number.
    prompt("What's the second number?")
    num2 = input()

    while invalid_number(num2):
        prompt(messages('invalid_number', language))
        num2 = input()

    #Ask the user for an operation to perform

    prompt("""What operation would you like to perform
    1) Add 2) Subtract 3) Multiply 4) Divide""")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1':
            output = float(num1) + float(num2)
        case '2':
            output = float(num1) - float(num2)
        case '3':
            output = float(num1) * float(num2)
        case '4':
            output = float(num1) / float(num2)

    print(f'The result is {output}')
    print("""Would you like to perform another calculation?
Enter 1 for yes or 2 for no""")
    continue_or_not = input()
    match continue_or_not:
        case '1':
            want_to_calculate = True
        case '2':
            want_to_calculate = False

# Currently, our calculator asks the user for two numbers and an operation and then exits after displaying the result. Wouldn't it be nice if we could ask the user if they wanted to perform another calculation and start a new calculation when they respond with yes?

