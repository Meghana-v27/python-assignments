a=[4,7,2,9,1]
b=[8,2,1,6,4]
for i in a:
    for j in b:
        if i==j:
            print(i)
#-------------------
arr=[2,5,7,9,1,4]
target=11
for i in arr:
    for j in arr:
        if i+j==target:
            print(f'{i} {j}')
            break
    break
#------------------------------------
arr=["apple","banana","apple","orange","banana","apple"]
elements=[]
for i in arr:
    if i not in elements:
        count=0
        for j in arr:
            if i==j:
                count+=1
        print(f'{i}: {count}')
        elements+=[i]
#-----------------------------------------------
names=["Raj","John","Raj","Mike","John","Raj"]
elements=[]
for i in names:
    if i not  in elements:
        count=0
        for j in names:
            if i==j:
                count+=1
        if count!=1:
            elements+=[i]
for i in elements:
    print(i)
#----------------------------------------------------
m1=[[1,2,3],[4,5,6]]
m2=[[1,2,3],[4,5,6]]
first=[]
second=[]
for i in m1:
    for j in i:
        first+=[j]
for k in m2:
    for l in k:
        second+=[l]
if first==second:
    print("Matrices are equal")
else:
    print("Matrices are not equal")
#---------------------------------------------------
a=[1,2,3,4,5,6]
b=[2,4,6]
l=[]
for i in a:
    for j in b:
        if i==j and i not in l:
            break
    else:
        l+=[i]
for i in l:
    print(i)
#--------------------------------------
        
