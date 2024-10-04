#Task 1 of 1: Leap Year Explorer

year = int(input("Enter the year you want to determine the leap year status of:"))


if (year % 4 == 0 and year % 100 != 0):
    print("The year you entered is, in fact, a Leap Year!")
elif (year % 400 == 0):
    print("The year you entered is, in fact, a Leap Year!")
else: 
    print("The year you entered is NOT a Leap Year!")