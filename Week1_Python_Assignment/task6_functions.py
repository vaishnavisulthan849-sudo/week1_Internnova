
def square(number):
    return number * number


def average(a, b, c):
    return (a + b + c) / 3


n = float(input("Enter a number to find its square: "))
print("Square:", square(n))

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = float(input("Enter the third number: "))

print("Average:", average(x, y, z))
