# Capstone Project: Personal Finance Tracker
print("Welcome to the Personal Finance Tracker!\n")

expenses = {}

#Create a method that adds an expense
def add_expense(descp, category, amount):
    if category not in expenses:
        expenses[category] = [(descp, amount)]
    else:
        expenses[category].append((descp, float(amount)))

def view_all_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return
    for category, items in data.items():
        print(f"Category: {category}")
        for descp, amount in items:
            print(f"  - {descp}: ${amount:.2f}")

def view_category_expenses(data):
    for category in data:
        total_amount = sum([expense[1] for expense in data[category]])
        print(f"{category}: ${total_amount}")

while True:
    def get_option():
        try:
            option = int(input("What would you like to do? \n1. Add Expense \n2. View All Expenses \n3. View Summary \n4. Exit \nChoose an option: "))
            print("\n")
            return option
        except ValueError: #If you didn't enter an integer-based option.
            print("\n")
            return -1
    
    option = get_option()
    if option == 4: #Exit
        print("Goodbye!")
        break
    elif not (option >= 1 and option <= 4): #Invalid option
        if option == -1:
            print("An option strictly has to be a number. Please try again.")
            print("\n")
            continue
        else:
            print("Invalid option. Please try again.")
            print("\n")
            continue
         
    #Performing the menu options.
    if option == 1: #Add expense
        #Ask user to enter description, category, and amount
        expense_descp = input("Enter expense description:")
        category = input("Enter category:")
        while True:
            try:
                amount = float(input("Enter amount:"))
                if amount <= 0:
                    print("Invaid amount. Please enter an amount greater than 0.")
                    continue
                break  # Exit loop if amount is valid
            except ValueError:
                print("Invalid amount. Please enter a numeric value (e.g., 12.50)")
        add_expense(expense_descp, category, amount)
        print("Expense added successfully.")
    elif option == 2: #View all expenses
        # Create a function that views all expenses and call it here.
        view_all_expenses(expenses)
    elif option == 3: #View summary
        view_category_expenses(expenses)
    print("\n")
