# Python calculator by Nimer

# Settings

# Defines calculator mode. Modes: (add, subtract, multiply, and divide). Replace value to set mode.
mode = "add"
# First number in equation.
firstNumber = float(2)
# Second number in equation. also where you put your percentage
secondNumber = float(1)

# Code

# Used to calculate the percentage.
percentage = secondNumber / 10

# Checks for what mode you're on.
if mode == "add":
    print("mode is add!")
    print(firstNumber, "+", secondNumber, "=", firstNumber + secondNumber)

elif mode == "subtract":
    print("mode is subtract!")
    print(firstNumber, "-", secondNumber, "=", firstNumber - secondNumber)

elif mode == "multiply":
    print("mode is multiply!")
    print(firstNumber, "x", secondNumber, "=", firstNumber * secondNumber)

elif mode == "division":
    print("mode is division!")
    print(firstNumber, "÷", secondNumber, "=", firstNumber / secondNumber)
elif mode == "percent":
    print("mode is percentage!")
    print("percentage is ", firstNumber * secondNumber)

else:
    print("Error! are you sure the mode that you selected exists?")