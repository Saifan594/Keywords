print("\033c")

def dueAmount(actual_amount, given_amount):
    return actual_amount - given_amount

bill = int(input("Enter bill amount : $"))
paid = int(input("Enter paid amount : $"))

due_amount = dueAmount(bill, paid)

print(f"Due Amount : ${due_amount}")