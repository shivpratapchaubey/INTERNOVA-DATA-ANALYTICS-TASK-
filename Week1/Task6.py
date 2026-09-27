def square(number):
    return number * number


def average(a, b, c):
    return (a + b + c) / 3


num = float(input("Enter a number: "))
print("Square:", square(num))

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

print("Average:", average(x, y, z))