# Capstone Project: Personal Finance Tracker
print("Welcome to the Personal Finance Tracker!\n")

while True:
    option = int(input("What would you like to do? \n1. Add Expense \n2. View All Expenses \n3. View Summary \n5. Exit >"))
    print("\n")
    if option == 5: #Exit
        print("Goodbye!")
        break
    elif not (option >= 1 and option <= 5): #Invalid option
        print("Invalid option. Please try again.")
        print("\n")
        continue
    
    #Keep entering the numbers till it's valid.
    while True:
        try:  
            first_num = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    while True:
        try:  
            second_num = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    #Performing the menu options.
    if option == 1: #Addition
        print(f"The sum of {first_num} and {second_num} is {first_num + second_num:.2f}.")
    elif option == 2: #Subtraction
        print(f"The difference between {first_num} and {second_num} is {first_num - second_num:.2f}.")
    elif option == 3: #Multiplication
        print(f"The product of {first_num} and {second_num} is {first_num * second_num:.2f}.")
    elif option == 4: #Division
        try:
            print(f"{first_num} divided by {second_num} is {first_num / second_num:.2f}.")
        except ZeroDivisionError:
            print("Oops! Division by zero is not allowed.")
    print("\n")
