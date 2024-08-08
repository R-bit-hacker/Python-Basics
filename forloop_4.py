for i in range(5):
    print("Are you tired?")
    tired = input("only yes/no: ")
    while tired not in ["yes", "no"]:
        print("Invalid input")
        tired = input("only yes/no: ")
    
    if tired == "yes":
        break
    # If the input is "no", continue to the next iteration (implicitly)

if i == 4:
    print("Congratulations you have completed the race")
else:
    print(f"You didn't complete the race but hurray as you completed {i + 1} km")
