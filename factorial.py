a=int(input("Enter a number:"))
for i in range(1,a):
    a*=i
print(a)


#the normal method appears to be faster and more efficent. 
#the amount of multiplication remains same in both methods but the cat of calling the 
#same function over and over again makes recursion slower.
