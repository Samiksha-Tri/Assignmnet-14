#Write a Python script to find the greatest number in a given list of numbers.
print("enter list elements seperated by comma:")
l1=[int(e) for e in input().split(',')]
max=l1[0]
for a in l1:
    if max<a:
        max=a
print("list is : ",l1)        
print("max element is: ",max)        