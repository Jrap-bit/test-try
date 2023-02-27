def addition(numbers):
    add = numbers[0]
    for i in range(1, len(numbers)):
        add = add + numbers[i]
    return add

def divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is undefined")
