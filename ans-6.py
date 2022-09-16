#Write a Python script to calculate the sum of elements in a given list of numbers.
print("enter list elements seperated by comma:")
l1=[int(e) for e in input().split(',')]
sum=0
for a in l1:
    sum=sum+a
print("list is : ",l1)        
print("sum is: ",sum)