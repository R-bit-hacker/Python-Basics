import numpy as np
exp=[2200,2350,2600,2130,2190]
arr=np.array(exp)
print(arr)
#1
print("Extra dollars spent in FEB as compared to JAN: ", arr[1]-arr[0])
#2
print("Total expense in 1st quarter of the year: ", arr[0]+arr[1]+arr[2])
#3
val=int(input("Enter the value you want to find: "))
print(f"Did I spend ${val} in any month?",val in arr)
for i in range(len(arr)):
    if val==arr[i]:
        print(f"You spent ${val} in {i+1} month")
#4
arr=np.append(arr,1980)
print(arr)
#5
arr[3]=arr[3]-200
print(arr)