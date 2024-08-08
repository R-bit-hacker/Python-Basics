#PYTHON LISTS

india = ["mumbai", "delhi", "chennai"]
pakistan = ["lahore", "islamabad", "karachi"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("Enter a city: ")

if city in india:
   print(f"{city} belongs to INDIA")
elif city in pakistan:
   print(f"{city} belongs to PAKISTAN")
elif city in bangladesh:
   print(f"{city} belongs to BANGLADESH")
else:
   print(f"based on my limited knowledge i cant tell that to which country {city} belongs to")