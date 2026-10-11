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
    name = input("Enter the name of the finance record: ")
    record_type = input("Enter the type (income/expense): ")
    amount = float(input("Enter the amount: "))

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
    save_finances(finances)

    if finance_to_remove:
        finances.remove(finance_to_remove)
        return True
    else:
        return False

def save_finances(finances):
    with open("finances.json", "w") as file:
        json.dump(finances, file, indent=4)
    print("Finances saved successfully.")

