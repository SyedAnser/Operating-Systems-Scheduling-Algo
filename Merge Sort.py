def m(a,p,q,r):
    x1=q-p+1
    x2=r-q
    A=[0]*x1
    B=[0]*x2
    for i in range(0,x1):
        A[i]=a[p+i]
    for j in range(0,x2):
        B[j]=a[q+1+j]
    i=0
    j=0
    k=p
    while i<x1 and j<x2:
        if A[i]<=B[j]:
            a[k]=A[i]
            i+=1
        else:
            a[k]=B[j]
            j+=1
        k+=1
    while i<x1:
        a[k]=A[i]
        i+=1
        k+=1
    while j<x2:
        a[k]=B[j]
        j+=1
        k+=1

def MergeSort(a,p,r):
    if p<r:
        n=p+(r-p)//2
        MergeSort(a,p,n)
        MergeSort(a,n+1,r)
        m(a,p,n,r)

x=eval(input("Enter list of elements:"))
c=len(x)
MergeSort(x,0,c-1)
print(x)


