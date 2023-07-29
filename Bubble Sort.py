def bubbleSort(arr):
    n= len(arr)
    count=0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1            
    if count==0:
        print("best case")
    elif count==n*(n-1)/2:
        print("worst case")
    else:
        print("average case")


x=eval(input("enter array in square brackets:"))
bubbleSort(x)
print(x)




# Best case[sorted array input] complexity:
#     Time=O(n)
#     Space=O(1)

# Worst case[reverse sorted array input] complexity:
#     Time=O(n^2)
#     Space=O(1)