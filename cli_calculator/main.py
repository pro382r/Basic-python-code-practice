print("\n...Calculator...\n")

from calculator import calculate

def history():
   with open("history.txt", "a") as file:
      file.write(f"{a} {operator} {b} = {result}\n")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ").strip()

result = calculate(a, operator, b)
print(f"Result: {result}")

history()

print("\n--------------------------------\n")
