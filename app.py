num1 = float(input("Enter num1 value: "))
num2 = float(input("Enter num2 value: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"


print("Addition of num1 and num2:", addition)
print("Subtraction of num1 and num2:", subtraction)
print("Multiplication of num1 and num2:", multiplication)
print("Division of num1 and num2:", division)
