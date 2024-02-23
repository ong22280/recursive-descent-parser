# E -> T | T + E
def E(tokens):
    global index
    if index >= len(tokens):
        print("reject")
        exit()
    
    # T
    T(tokens)
    
    # T + E
    if index < len(tokens) and tokens[index] == '+':
        index += 1
        if index >= len(tokens):
            print("reject")
            exit()
        E(tokens)

# T -> int | int * T | (E)
def T(tokens):
    global index
    if index >= len(tokens):
        print("reject")
        exit()
    
    # int
    if tokens[index] == 'int':
        index += 1
        
        # int * T
        if index < len(tokens) and tokens[index] == '*':
            index += 1
            if index >= len(tokens):
                print("reject")
                exit()
            T(tokens)
            
    # (E)
    elif tokens[index] == '(':
        index += 1
        E(tokens)
        if index < len(tokens) and tokens[index] == ')':
            index += 1
        else:
            print("reject")
            exit()

def recursive_descent_parser(tokens):
    global index
    
    E(tokens)
    if index == len(tokens):
        print("accept")
    else:
        print("reject")

input_string = input("Enter a sequence of symbols separated by space: ")
tokens = input_string.split()
index = 0
recursive_descent_parser(tokens)