#Write a Python script to remove all non int values from a list.
l1=[1,3,6.4,True,'akash',9]
print("list is : ",l1)
l2=[]
for e in l1:
    if type(e)==int:
        l2.append(e)   
print("final list without integer values : ",l2)        

