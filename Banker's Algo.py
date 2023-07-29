import numpy as np

def condition_check(i):
    for j in range(num_resource):
        if(need[i][j]>avail[j]):
            return 0
    return 1


num_process = 5
num_resource = 4

safe_seq = np.zeros((num_process,),dtype=int)
checked = np.zeros((num_process,),dtype=int)

alloc = np.array([[2,0,0,1],[3,1,2,1],[2,1,0,3],[1,3,1,3],[1,4,3,2]])
max = np.array([[4,2,1,2],[5,2,5,2],[2,3,1,6],[1,4,2,4],[3,6,6,5]])

need = max - alloc
avail = np.array([3,3,2,1])

done = 0
while( done < num_process ):
    x=0
    for i in range( num_process ):
        if( checked[i] == 0 ):
            if(condition_check(i)):
                safe_seq[done]=i
                done+=1
                checked[i]=1
                x=1
                for j in range(num_resource):
                    avail[j] += alloc[i][j] 
                break
    if(x == 0):
        break


if(done < num_process):
    print('System ---> Unsafe')
else:
    print("System ---> Safe")
    print("Sequence: ",safe_seq)
    print("Available Resource:",avail)