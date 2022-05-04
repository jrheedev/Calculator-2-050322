"""CLI application for a prefix-notation calculator."""


from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True: 
    string = input("Which action would like you to perform?")
    tokens = string.split(' ')

    if tokens[0] == 'q':
        break
    
    if tokens[0] == '+':
        int(tokens[1])
        int(tokens[2])
        print(tokens[1] + tokens[2])

    if tokens[0] == '-':
        int(tokens[1])
        int(tokens[2])
        print(tokens[1] - tokens[2])

    if tokens[0] == '*':
        int(tokens[1])
        int(tokens[2])
        print(tokens[1] * tokens[2])
    
    else: 
        print("Sorry, I don't understand")

