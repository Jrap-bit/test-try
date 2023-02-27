import Sub_Mult as sub_mult
import Add_Divide as add_divide


if __name__ == '__main__':
    print("\t\t This is a Simple Calculator \t\t")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Enter the numbers to be added")
        nums = int(input("How many numbers do you want to add?: "))
        num_arr = []
        for i in range(nums):
            num_arr.append(int(input(("Enter number {} to add: ".format(i + 1)))))
        print("Sum = ", add_divide.addition(num_arr))
    elif choice == 2:
        print("Enter the numbers to be subtracted")
        nums = int(input("How many numbers do you want to subtract?: "))
        num_arr = []
        for i in range(nums):
            num_arr.append(int(input(("Enter number {} to subtract: ").format(i + 1))))
        print("Difference = ", sub_mult.subtract(num_arr))
    elif choice == 3:
        nums = int(input("How many numbers do you want to multiply?: "))
        num_arr = []
        for i in range(nums):
            num_arr.append(int(input(("Enter number {} to multiply: ").format(i + 1))))
        print("Product = ", sub_mult.multiply(num_arr))
    elif choice == 4:
        print("Enter the numbers to be divided")
        num1 = int(input())
        num2 = int(input())
        print("Quotient = ", add_divide.divide(num1, num2))
    elif choice == 5:
        exit()