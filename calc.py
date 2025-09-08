def add(a, b):
    result = a + b
    if result % 1 != 0:
        return result
    
    else:
        return int(result)

def subtract(a, b):
    result = a - b
    if result % 1 != 0:
        return result
    
    else:
        return int(result)

def multiply(a, b):
    result = a * b
    if result % 1 != 0:
        return result
    
    else:
        return int(result)

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    
    result = a / b

    if result % 1 != 0:
        return result
    
    else:
        return int(result)