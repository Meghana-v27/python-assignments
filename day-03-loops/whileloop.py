# Create a Python program that uses a while loop to ask the user for a number until they enter a positive integer.
num=input("Enter a number :")
while not num.isdigit() or int(num)<0:
    print("Invalid input!!")
    num=(input("Please enter a postive number:"))

# Once a positive integer is entered, use a while loop to calculate and print the sum of all numbers from 1 up to the entered number.
num=int(num)
total=0
i=1
while i<=num:
    total+=i
    i+=1
print("sum of 1 to ",num,"is ",total)