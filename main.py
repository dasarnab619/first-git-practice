
from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

calculator_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}