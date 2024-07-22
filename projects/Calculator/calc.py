from art import logo
def add(one, two):
    return one+two

def sub(one, two):
    return one-two

def mult(one, two):
    return one*two

def div(one, two):
    return one/two

d = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in d:
        print(key)
    while True:
        symbol = input("Pick an operation from the above: ")
        num2 = float(input("What's the next number?: "))
        ans = d[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {ans}")
        repeat = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation.: ")
        if repeat == 'y':
            num1 = ans
        else:
            calculator()
        

calculator()


    
