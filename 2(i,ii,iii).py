#CONDITIONS  -IF, -ELIF, -ELSE

sugar_level = float(input("Enter your Fasting sugar level: "))

if sugar_level < 80:
    print(f"sugar is {sugar_level} and is low")
elif sugar_level >100:
    print(f"sugar is {sugar_level} and is high")
else:
    print(f"sugar is {sugar_level} and is normal")