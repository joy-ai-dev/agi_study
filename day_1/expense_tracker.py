expense_val = 0
while expense_val != "done":
    expense_num = int(expense_val)
    if expense_num >= 2000:
        print("Warning: You've overspent!!!")
    elif expense_num >= 1000:
        print("That was a big spend!")
    expense_val = input ("Enter an expense (₹) or 'done' to finish:")

