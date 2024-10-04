#Task 1 - Task 2

#Task 1 - Identify the Greatest:


num_1 = float (input("Enter first number:"))
num_2 = float (input("Enter second number: "))
num_3 = float (input("Enter third number: "))

if (num_1 >= num_2) and (num_1 >= num_3):
   largest = num_1
elif (num_2 >= num_1) and (num_2 >= num_3):
   largest = num_2
else:
   largest = num_3
print("The largest number is", largest)



#Task 2: Identify the Smallest

num_1 = float(input("Enter first number:"))
num_2 = float(input("Enter second number: "))
num_3 = float(input("Enter third number: "))

if (num_1 <= num_2) and (num_1 <= num_3):
   smallest = num_1
elif (num_2 <= num_1) and (num_2 <= num_3):
   smallest = num_2
else:
    smallest = num_3
print("The smallest number is", smallest, "The largest number is", largest)


#Couldn't figure out how to only have 3 inputs vs 6

#Maybe I'm just having a moment BUT
#I couldn't figure out how to correctly add a "." to seperate 
#the sentences "The smaller number is xxx" and "The largest number is xxx"
#Lol