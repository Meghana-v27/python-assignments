i=1
#while loop to iterate over a range of numbers from 1 to 10
while i<=10:
    #to print even numbers
    if i%2==0:
        print(i)
    #continue statement to skip the odd numbers
    if i%2!=0:
        i+=1
        continue
    # to terminate a loop using break if num is 8
    if i==8:
        break
    i+=1