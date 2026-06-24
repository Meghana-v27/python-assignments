#valid ages
ages=[]
count=0
active=True
while active:
    age=int(input("Enter age:"))
    if age==-1:
        active=False
        continue
    if age>0 and age<120:
        count+=1
print("valid ages count:",count)
#---------------------------------------------------------
# sum multiples of  5
sum=0
T=True
while T:
    num=int(input("Enter number: "))
    if num==0:
       T=False
       continue
    if num%5!=0:
        continue
    else:
        sum+=num
print("Sum:",sum)
#---------------------------------------------------------

#count Uppercase letters
text="pyTHon ProGRAM"
upper=0
for ch in text:
    if 'a'<ch<'z':
        continue
    else:
        upper+=1
print("Uppercase Letters count: ",upper)
#---------------------------------------------------------
#total sales amount
sales=[500,0,1200,0,700]
total=0
for sale in sales:
    if sale==0:
        continue
    else:
        total+=sale
print("Total sales amount: ",2400)
