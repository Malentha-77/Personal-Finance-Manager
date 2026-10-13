import json

with open("finances.json", "r") as file:
    finances = json.load(file)

print(finances)

def get_total_income(finances):
    total = 0

    for finance in finances:
        if finance['type'] == "income":
            total += finance['amount']

    return total

def get_total_expenses(finances):
    total = 0

    for finance in finances:
        if finance['type'] == "expense":
            total += finance['amount']

    return total

def get_balance(finances):
    income = get_total_income(finances)
    expenses = get_total_expenses(finances)

    answer = income - expenses
    return answer

def find_finance(finances, name):
    for finance in finances:
        if finance['name'] == name:
            return finance
    return None

def count_finances(finances, record_type):
    count = 0

    for finance in finances:
        if finance['type'] == record_type:
            count += 1
    return count

def show_finances(finances):
    for finance in finances:
        print(f"Name: {finance['name']}, Type: {finance['type']}, Amount: {finance['amount']}")

def add_finance(finances):
    name = input("Enter the name of the finance record: ").strip()
    if not name.strip():
        print("Name cannot be empty.")
        return
    
    record_type = input("Enter the type (income/expense): ")
    while record_type != "income" and record_type != "expense":
        print("Invalid type. Please enter 'income' or 'expense'.")
        record_type = input("Enter the type (income/expense): ")

    while True:
        try:
            amount = float(input("Enter the amount: "))

            if amount <= 0:
                print("Amount must be a positive number.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    new_finance = {
        "name": name,
        "type": record_type,
        "amount": amount
    }

    finances.append(new_finance)
    save_finances(finances)
    print("Finance record added successfully.")

def remove_finance(finances, name):
    finance_to_remove = find_finance(finances, name)
    
    if finance_to_remove:
        finances.remove(finance_to_remove)
        save_finances(finances)
        return True
    else:
        return False

def save_finances(finances):
    with open("finances.json", "w") as file:
        json.dump(finances, file, indent=4)
    print("Finances saved successfully.")

def menu(finances):
    choice = ""
    while choice != "8":
        print("\n=== Personal Finance Management Menu ===")
        print("1. Show all finances")
        print("2. Add a finance record")
        print("3. Remove a finance record")
        print("4. Find a finance record")
        print("5. Show total income")
        print("6. Show total expenses")
        print("7. Show balance")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            show_finances(finances)

        elif choice == "2":
            add_finance(finances)

        elif choice == "3":
            name = input("Enter the name of the finance record to remove: ")
            if remove_finance(finances, name):
                print("Finance record removed successfully.")
            else:
                print("Finance record not found.")

        elif choice == "4":
            name = input("Enter the name of the finance record to find: ")
            finance = find_finance(finances, name)
            if finance:
                print(f"Finance record found: Name: {finance['name']}, Type: {finance['type']}, Amount: {finance['amount']}")
            else:
                print("Finance record not found.")

        elif choice == "5":
            total_income = get_total_income(finances)
            print(f"Total income: R{total_income}")

        elif choice == "6":
            total_expenses = get_total_expenses(finances)
            print(f"Total expenses: R{total_expenses}")

        elif choice == "7":
            balance = get_balance(finances)
            print(f"Balance: R{balance}")

        elif choice == "8":
            print("Exited...")
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

menu(finances)