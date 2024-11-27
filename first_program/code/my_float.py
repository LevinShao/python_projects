num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
answer = input("What would u like to do? +, -, x or /?")

if answer == "+":
    print(num1 + num2)
if answer == "-":
    print(num1 - num2)
if answer == "x":
    print(num1 * num2)
if answer == "/":
    print(num1 / num2)
else:
    print("I'm sorry, I don't understand")