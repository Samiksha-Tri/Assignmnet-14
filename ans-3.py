#Write a Python script to create a list of first N even natural numbers.
n=int(input("enter number of even natural number list you want to create : "))
i=2
l1=[]
while i<=(n*2):
    l1.append(i)
    i+=2
print(l1)