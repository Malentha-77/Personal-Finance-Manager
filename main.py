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
