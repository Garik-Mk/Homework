import sys

def polish_notation(arguments_list):
    arguments_list = str(arguments_list)
    arguments_list = arguments_list.split(' ')
    operator = arguments_list[0]
    number1 = int(arguments_list[1])
    number2 = int(arguments_list[2])
    if operator == '+':
        return number1 + number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    elif operator == '-':
        return number1 - number2
    elif operator == '%':
        return number1 % number2
    elif operator == '//':
        return number1 // number2
    else:
        print('error: Wrong operator')


for command in iter(sys.stdin.readline, ''):
    command = command[:-1]
    if command == "exit":
        break
    print(polish_notation(command))
    