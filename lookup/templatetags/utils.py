def calculate_total(price, quantity):
    return price * quantity

# math_operations/utils.py

def calculate(operation, num1, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"
    
    return result
