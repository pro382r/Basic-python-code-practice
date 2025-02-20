def greet(name):
    return "Hello, " + name + "!"

message = greet("Bob")
print(message)

def add(x, y):
    return x + y

result = add(5, 3)
print("Sum:", result)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
