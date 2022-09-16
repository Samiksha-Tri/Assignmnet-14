""" Write a Python script to print indices of all occurrences of a given element in a given
list.
"""

l1=[3,3,2,2,2,5,7,9,9,9,4]  #given list
e=int(input("enter element of the list for which index of occurences you want :"))
i=0
while i<len(l1):
    if l1[i]==e:
        print("index: ",i,end='\n')
    i=i+1