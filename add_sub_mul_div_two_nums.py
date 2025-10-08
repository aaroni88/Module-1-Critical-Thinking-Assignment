
# Aaron Isaac
# Module 1: Critical Thinking Assignment
# This program will add, subtract, multiply, and divide any two given numbers


# Part 1: Addition and Subtraction
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2

print("Addition result:", addition)
print("Subtraction result:", subtraction)

# Part 2: Multiplication and Division
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    print("Multiplication result:", multiplication)
    print("Division result:", division)
else:
    print("Multiplication result:", multiplication)
    print("Division by zero is not allowed.")
