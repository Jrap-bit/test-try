import Functional_Files.calc as c

if __name__ == "__main__":
    exp = input(
        "Enter the Expression to be Evaluated (Each Value Separated by space): ")
    var1, op, var2 = exp.split()
    var1, var2 = int(var1), int(var2)
    res = "Error."
    if op == '+':
        res = c.add(var1, var2)
    elif op == '-':
        res = c.sub(var1, var2)
    elif op == '*':
        res = c.mul(var1, var2)
    elif op == '/':
        res = c.div(var1, var2)
    elif op == '%':
        res = c.mod(var1, var2)
    elif op == '**':
        res = c.pow(var1, var2)
    else:
        print("Invalid Operator")

    print(res)
