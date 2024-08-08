indian=["samosa", "panipuri", "vara pau"]
pakistani=["biryani", "nihari", "siripaye"]
arabian=["mandi", "kunafa", "baklavah"]

dish=input("Enter a dish name:" )

if dish in indian:
   print(f"{dish} is INDIAN")
elif dish in pakistani:
   print(f"{dish} is PAKISTANI")
elif dish in arabian:
   print(f"{dish} is ARABIAN")
else:
   print(f"based on my limited knowledge, i dont know hich cuidine is {dish}")
