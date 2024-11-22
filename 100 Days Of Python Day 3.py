# Prompt the user to enter a year and display a message
print("Enter a year:")

# Read the user input, convert it to an integer, and store it in the variable `year`
year = int(input())

# Check if the year is divisible by 4, a primary condition for leap years
if year % 4 == 0:
    # If divisible by 4, check if the year is divisible by 100
    if year % 100 == 0:
        # If divisible by 100, check if the year is also divisible by 400
        if year % 400 == 0:
            # If divisible by 400, it is a leap year
            print("It is a leap year")
        else:
            # If divisible by 100 but not by 400, it is not a leap year
            print("It is not a leap year")
    else:
        # If divisible by 4 but not by 100, it is a leap year
        print("This is a leap year.")
else:
    # If not divisible by 4, it is not a leap year
    print("Not a leap year")

