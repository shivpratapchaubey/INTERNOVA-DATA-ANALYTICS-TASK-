a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n----- Calculator Result -----")
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)

if b != 0:
    print("Division       :", a / b)
    print("Modulus        :", a % b)
else:
    print("Division       : Not possible")
    print("Modulus        : Not possible")