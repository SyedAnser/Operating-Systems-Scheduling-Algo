def add(x,y):
    mat=[]
    for i in range(len(x)):
        res=[]
        for j in range(len(x[0])):
            res.append(0)
        mat.append(res)
    

    for i in range(len(x)):
        for j in range(len(x[0])):
            mat[i][j]=x[i][j]+y[i][j]
    print(mat)


def substract(x,y):
    mat=[]
    for i in range(len(x)):
        res=[]
        for j in range(len(x[0])):
            res.append(0)
        mat.append(res)
    

    for i in range(len(x)):
        for j in range(len(x[0])):
            mat[i][j]=x[i][j]-y[i][j]
    print(mat)


def multiply(x,y):
    mat=[]
    for i in range(len(x)):
        res=[]
        for j in range(len(y[0])):
            res.append(0)
        mat.append(res)
     

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                mat[i][j]+=x[i][k]*y[k][j]
    print(mat)    


x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,2],[6,7,3],[4,5,9]]

add(x,y)
substract(x,y)
multiply(x,y)



#The time complexity of each of these funtions is as follows:
# Matrix Addition: O(n^2)
# Matrix Substraction: O(n^2)
# Matrix Multiplication: O(n^3)