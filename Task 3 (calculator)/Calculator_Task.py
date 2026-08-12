def check_first_num(n1):
    while not (n1.isnumeric()):
        n1 = input("Enter the first number again: ")
    return int(n1)

def check_second_num(n2):
    while not (n2.isnumeric()):
        n2 = input("Enter the second number again: ")
    return int(n2)
    

def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def division(n1,n2):
    if n2 == 0:
        return "Error: Division by zero"
    else: return n1/n2

x = 1
print("Welcome to The Simple Calculator!")

while x:

    num_1 = input("Enter the first number: ")
    num_1 = check_first_num(num_1)

    num_2 = input("Enter the second number: ")
    num_2 = check_second_num(num_2)

    print("1- Addition")
    print("2- Subtrction")
    print("3- Multiplication")
    print("4- Division")

    choice = int(input("What do you want? "))

    check = 1
    while check:
        if choice in range(1,5):
            check = 0
            if choice == 1:
                result = addition(num_1,num_2)
                print(f"The result of adding {num_1} and {num_2} is {result}")

            elif choice == 2:
                result = subtraction(num_1,num_2)
                print(f"The result of subtracting {num_1} and {num_2} is {result}")

            elif choice == 3:
                result = multiplication(num_1,num_2)
                print(f"The result of multiplicating {num_1} and {num_2} is {result}")

            elif choice == 4:
                result = division(num_1,num_2)
                print(f"The result of dividing {num_1} and {num_2} is {result}")

        else: 
            print("Invalid input, Enter again.")
            choice = int(input("What do you want? "))

    again = input("Do you wany to perform another calculation (yes/no)? ").lower()

    if again == "yes":
        x = 1
    elif again == "no":
        x = 0
        print("Good bye!")
