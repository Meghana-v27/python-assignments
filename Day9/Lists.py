num=48391
number=[]
result=[]
while num>0:
    rem=num%10
    number=[rem]+number
    num//=10
if  len(number)%2==1:
    i=0
    while i<=(len(number)//2):
        if i==(len(number)//2):
            result+=[number[i]]
            break
        else:
            result+=[number[i]+number[-1-i]]   
        i+=1
print(result)
# #----------------------------------------
num=int(input("Enter a number:"))
frequency={}
while num>0:
    rem=num%10
    if rem in frequency:
        frequency[rem]+=1
    else:
        frequency[rem]=1
    num//=10
for val in frequency.values():
    if val==1:
        print(val)
# #---------------------------------------------------
num=int(input("Enter a number:"))
number=[]
while num>0:
    rem=num%10
    number=[rem]+number
    num//=10
length=len(number)
i=0
while i<length-1 and number[i]<number[i+1]:
    i+=1
if i==0 or i==length-1:
    print(False)
else:
    while i<length-1 and number[i]>number[i+1]:
        i+=1
    if i==length-1:
        print(True)
    else:
        print(False)
# #----------------------------------------------------
n=int(input("Enter a number"))
temp=n
rev=0
num=[]
while n>0:
    rem=n%10
    num=[rem]+num
    rev=rev*10+rem
    n//=10
i=0
for i in range(len(num)):
    for j in range(0,len(num)-i-1):
        if num[j]<num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
high=int(''.join(map(str,num)))
i=0
for i in range(len(num)):
    for j in range(0,len(num)-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
low=0
for x in num:
    low=low*10+x
print("Rotations:")
print(temp)
print(rev)
print(high)
print(low)
print("Largest rotation is:")
if temp>rev and temp>high and temp>low:
    print(temp)
elif rev>temp and rev>high and rev>low:
    print(rev)
elif high>temp and high>low and high>rev:
    print(high)
else:
    print(low)
# #-----------------------------------------
n=82746
num=[]
while n>0:
    rem=n%10
    num=[rem]+num
    n//=10
x=0
sum=0
while x<len(num)-1:
    diff=num[x]-num[x+1]
    if diff<0:
        diff*=-1
    sum+=diff
    x+=1
print(sum)
#-----------------------------------------
n=2345
num=[]
while n>0:
    rem=n%10
    num=[rem]+num
    n//=10
x=0
number=0
while x<len(num)-1:
    prod=num[x]*num[x+1]
    if prod>9:
        number=(number*100)+prod
    else: number=(number*10)+prod
    x+=1
print(number)
# #---------------------------------
n=1638
num=[]
while n>0:
    rem=n%10
    num=[rem]+num
    n//=10
x=0
while x<len(num)-1:
    diff=num[x]-num[x+1]
    if diff<0:
        diff*=-1
    true_count=0
    for i in range(2,diff):
        if diff%i!=0:
            true_count+=1
    x+=1
if true_count==len(num)-1:
    print(True)
else:
    print(False)
#--------------------------------------------------
num=462315
rev=[]
while num>0:
    rem=num%10
    rev=[rem]+rev
    num//=10
print(rev)
index=0
count=0
while index <(len(rev)-1):
    if index%2==0:
        if rev[index]<rev[index+1]:
            count+=1
    if index%2==1:
        if rev[index]>rev[index+1]:
            count+=1
    index+=1
if count==len(rev)-1:
    print(True)
else:
    print(False)
# #---------------------------------------------
num1=123456
num2=153406
match_count=0
while num1>0 and num2>0:
    rem1=num1%10
    rem2=num2%10
    if rem1==rem2:
        match_count+=1
    num1//=10
    num2//=10
print(match_count)
#--------------------------------------
num=12030405
zeros,n=0,0
p=1
while num>0:
    rem=num%10
    if rem==0:
        zeros+=1
    else:
        n=n+(rem*p)
        p*=10
    num=num//10
while zeros>0:
    print(0,end="")
    zeros=zeros-1
print(n)
#---------------------------------------------
