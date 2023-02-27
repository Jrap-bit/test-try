# SUBTRACTION
def subtract(numbers):
    diff = numbers[0]
    for i in range(1, len(numbers)):
        diff = diff - numbers[i]
    return diff


# MULTIPLICATION
def multiply(numbers):
    mult = 1
    for i in numbers:
        mult *= i
    return mult
