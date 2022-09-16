#Write a Python script to create a list of first N odd natural numbers.

n=int(input("enter number of odd natural number list you want to create : "))
i=1
l1=[]
while i<=(n*2):
    l1.append(i)
    i+=2
print(l1)