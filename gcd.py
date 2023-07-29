a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
x=True
if a>b:
    smaller=a
    larger=b
elif b>a:
    smaller=b
    larger=a
else:
    x=False
    gcd= a
    print(gcd)


while x:
    for i in range (1,smaller+1):
        if a%i==0 and b%i==0:
            gcd=i
            
    print(gcd)
    x=False

