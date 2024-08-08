month_list=["Jan", "Feb", "Mar","Apr","May"]
expense_list=[2340,2500,2100,3100,2980]

amount=int(input("Enter expense amount: "))

month=-1

for i in range(len(expense_list)):
    if amount==expense_list[i]:
        month=i
        break

if month!=-1:
    print(f"{amount} was spent in {month_list[month]}")

else:
    print(f"You didn't spend {amount} in any month")