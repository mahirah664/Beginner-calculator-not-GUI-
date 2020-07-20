def add(num1, num2):
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

def subtract(num1, num2):
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")

def multiply(num1, num2):
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")

def divide(num1, num2):
    total = num1 / num2
    print(f"{num1} / {num2} = {total}")

print("Hello. Welcome to this calculator.")
print("Please enter one of the following options:")
print("Enter '1' if you want to add two numbers. ")
print("Enter '2' if you want to subtract between two numbers. ")
print("Enter '3' if you want to multiply two numbers. ")
print("Enter '4' if you want to divide two numbers. ")

choice = False
while not choice:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num1 = float(input("What is the first number: "))
            num2 = float(input("What is the second number: "))
            add(num1, num2)
            choice = False
        elif choice == 2:
            num1 = float(input("What is the first number: "))
            num2 = float(input("What is the second number: "))
            subtract(num1, num2)
            choice = False
        elif choice == 3:
            num1 = float(input("What is the first number: "))
            num2 = float(input("What is the second number: "))
            multiply(num1, num2)
            choice = False
        elif choice == 4:
            num1 = float(input("What is the first number: "))
            num2 = float(input("What is the second number: "))
            divide(num1, num2)
            choice = False
        else:
            print("You did not enter a valid choice.")
            choice = False
    except ValueError:
        print("You did not enter a valid choice.")
    
