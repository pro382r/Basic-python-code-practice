def calculate(a, operator, b):
    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    else:
        raise ValueError("Invalid operator")


