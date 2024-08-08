def pattern_of_stars(number):
    for i in range(number + 1):
        for j in range(i):
            print("*", end="")
        print()
num= int(input("Enter a number for pattern: "))
pattern= pattern_of_stars(num)
print(pattern)