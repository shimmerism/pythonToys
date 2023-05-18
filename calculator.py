# Interactive calculator 1.0

# Import some libraries.
from math import sqrt

# Welcome Message.
print('--------------------------------------') 
print('Welcome to the calculator! Version 1.0')
print('--------------------------------------')

# Asks for math mode
print("Which mode do you want to use?")
mode = str(input("(add, subtract, multiply, divide, percent, exponent, and square root): "))
if mode == "add" or mode == "subtract" or mode == "multiply" or mode == "divide" or mode == "percent" or mode == "exponent" or mode == "square root":
    print('Mode exists!')

# Prints out an error message and exits if mode doesn't exist.
else:
    print ("--------------------------")
    print ("Error! mode doesn't exist.")
    print ("--------------------------")
    exit()

## Asks for numbers for equation.
# Gives a special message if mode is square root.
if mode != "square root":
    firstNumber = float(input("Enter the first number: "))
else:
    firstNumber = float(input("Enter a number: "))

# Disables second number if square root is chosen.
if mode != "square root":
    print("Enter the second number")
    secondNumber = float(input("(can be a number for the main 4 modes, a percentage *WITHOUT THE PERCENTAGE SYMBOL*, or an exponent): "))

# Checks for mode again and does equations.
if mode == "add":
    print("-------------------------------------------------------------")
    print(firstNumber, "+", secondNumber, "=", firstNumber + secondNumber)
    print("-------------------------------------------------------------")

if mode == "subtract":
    print("-------------------------------------------------------------")
    print(firstNumber, "-", secondNumber, "=", firstNumber - secondNumber)
    print("-------------------------------------------------------------")

if mode == "multiply":
    print("-------------------------------------------------------------")
    print(firstNumber, "x", secondNumber, "=", firstNumber * secondNumber)
    print("-------------------------------------------------------------")

if mode == "divide":
    print("-------------------------------------------------------------")
    print(firstNumber, "÷", secondNumber, "=", firstNumber / secondNumber)
    print("-------------------------------------------------------------")
if mode == "percent":
    percentage = secondNumber / 100
    print("-------------------------------------------------------------")
    print(secondNumber,"% of", firstNumber, "is", firstNumber * percentage)
    print("-------------------------------------------------------------")

if mode == "exponent":
    print("-----------------------------------------------------------------------------")
    print(firstNumber, "to the power of", secondNumber, "is", firstNumber ** secondNumber)
    print("-----------------------------------------------------------------------------")

if mode == "square root":
    print("--------------------------------------------------------")
    print("the square root of", firstNumber, "is", sqrt(firstNumber))
    print("--------------------------------------------------------")
