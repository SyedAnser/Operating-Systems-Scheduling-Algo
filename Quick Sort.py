def p(a, l, h):
    pivot=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<=pivot:
            i+=1
            (a[i],a[j])=(a[j],a[i])
    (a[i+1],a[h])=(a[h], a[i+1])
    return i+1

def QuickSort(a, l, h):
    if l<h:
        pi=p(a, l, h)
        QuickSort(a,l,pi-1)
        QuickSort(a,pi+1,h)

x=eval(input("Enter list of integers"))
s=len(x)
QuickSort(x,0,s-1)
print(x)