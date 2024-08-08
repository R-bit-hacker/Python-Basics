#PYTHON LIST

india = ["mumbai", "delhi", "chennai"]
pakistan = ["lahore", "islamabad", "karachi"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1=input("Enter 1st city: ")
city2=input("Enter 2nd city: ")

if city1 in india and city2 in india:
    print(f"both {city1} and {city2} belong to INDIA")
elif city1 in pakistan and city2 in pakistan:
    print(f"both {city2} and {city1} belong to pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print(f"both {city1} and {city2} belong to bangladesh")
else:
    print(f"{city1} and {city2} dont belong to same country")