
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Modulus:", a % b)
else:
    print("Division and modulus are not possible with zero.")
