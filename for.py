expenses = [1200,1500, 2000, 3500]
total=0

for i in range(len(expenses)):
    expense= expenses[i]
    print(f"Month: {i+1} Expense: {expense}")
    total += expense

print("Total expense: ", total)