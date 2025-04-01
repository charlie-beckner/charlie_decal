def add(a, b):
    '''Returns sum of a and b'''
    return a + b

def subtract(a, b):
    '''Returns difference of b subtracted from a'''
    return a - b

def multiply(a, b):
    '''Returns the product of a and b'''
    return a * b

def divide(a, b):
    '''Divides a by b and returns quotient. Returns "Error" if dividing by zero'''
    if b == 0:
        return "Error"
    else:
        return a / b 

