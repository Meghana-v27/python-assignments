# QUESTION 1: STUDENT MARKS TOTAL
# OBJECTIVE: Calculate and print the total marks scored across 3 subjects 
# for each of the 5 individual students using an accumulator inside a nested loop.
# 
# QUESTION 2: SHOP SALES REPORT
# OBJECTIVE: Collect daily sales data over a 7-day week for 4 distinct products
# and calculate the total accumulated weekly sales report for each item.
# 
# QUESTION 3: FIND HIGHEST MARK IN EACH STUDENT RECORD
# OBJECTIVE: Scan through 5 subject marks for 4 individual students and 
# use a conditional comparison check to isolate and display each student's highest mark.
# 
# QUESTION 4: THEATRE SEAT BOOKING STATUS
# OBJECTIVE: Iterate through a grid layout of theatre rows and seats to evaluate 
# booking statuses and provide a final aggregated count of booked versus empty seats.
#------------------------------------------------------------------------------
for i in range(1,6):
    for j in range(1,6):
        sum=i+j
        if sum%2==0:
            print(f'({i},{j})')
        else:
            continue
#-------------------------------------------------
i=1
while i<=5:
    j=1
    while j<=5:
        sum=i+j
        if sum%2==0:
            print(f'({i},{j})')
        else:
            j+=1
            continue
        j+=1
    i+=1
#--------------------------------------------------
i=1
count=0
while i<=10:
    j=1
    while j<=10:
        product=i*j
        if product>30:
            count+=1
            print(f'({i},{j}) -> {product}')
        else:
            j+=1
            continue
        j+=1
    i+=1
print("count of pairs =",count)
#--------------------------------------------------
num=-1
sum=0
while num!=0:
    print("\n")
    num=int(input("Enter a number:"))
    if num==0:
        break
    print(f"factors of {num} are:")
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
            sum+=i
        else:
            continue
print("sum:",sum)
