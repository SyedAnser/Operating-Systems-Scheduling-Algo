a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
while a%b!=0:
    r=a%b
    a=b
    b=r
print(b)



#the euclidean method is much more efficient than the regular method. 
#The regular method uses a lot comparisons that make it less efficient.