
from art import logo
print(logo)

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

math_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}
