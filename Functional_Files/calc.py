def add(var1, var2):
    return var1 + var2


def sub(var1, var2):
    return var1 - var2


def mul(var1, var2):
    return var1 * var2


def div(var1, var2):
    if var2 == 0:
        return "Cannot be divided by zero"
    return var1 / var2


def mod(var1, var2):
    if var2 == 0:
        return "Cannot be divided by zero"
    return var1 % var2


def pow(var1, var2):
    return var1 ** var2
