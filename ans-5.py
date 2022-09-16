#Write a Python script to find the smallest number in a given list of numbers.
print("enter list elements seperated by comma:")
l1=[int(e) for e in input().split(',')]
min=l1[0]
for a in l1:
    if min>a:
        min=a
print("list is : ",l1)        
print("minimum element is: ",min)        