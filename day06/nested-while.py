#problem1
i=1
while i<6:
    j=1
    while j<6:
        add=i+j
        if add%2==0:
            print(f'({i},{j})')
        j+=1
    i+=1
#------------------------------------------
#problem2
i=1
count=0
while i<11:
    j=1
    while j<11:
        if (i*j)>30:
            print(f'({i},{j}) -> {i*j}')
            count+=1
        j+=1
    i+=1
print("count :",count)
#--------------------------------------
#problem3
num=int(input("Enter a number:"))
while num!=0:
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            sum+=i
            print(i,end=" ")
    print()
    print("sum :",sum)
    num=int(input("Enter a number:"))
#--------------------------------------------------
#problem4
numbers=[12,7,20,9]
for num in numbers:
    count=0
    temp=num
    while temp>0:
        if temp%2==0:
            count+=1
        temp-=1
    print(f"{num} -> Even count:{count}")
