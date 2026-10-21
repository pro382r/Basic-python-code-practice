print("\n...Calculator...\n")

from calculator import calculate

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ").strip()

result = calculate(a, operator, b)
print(f"Result: {result}")


print("\n--------------------------------\n")
