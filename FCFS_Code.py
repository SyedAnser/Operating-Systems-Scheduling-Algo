import numpy as numpy



with open('C:/Users/syeda/Desktop/codes/fcfs.txt') as f:
    x=[]
    for line in f:
        line = line.split() # to deal with blank 
        line = [int(i) for i in line]
        x.append(line)

pid=x[0]
burst=x[1]
arrival=x[2]


s = numpy.array(arrival)
sort_index = numpy.argsort(s)

ch=0
Gantt=[]
for i in sort_index:
    ch+=burst[i]
    Gantt.append(ch)

print("Gantt Chart=", Gantt)

completion=[]
for i in sort_index:
    x=Gantt[i]
    completion.append(x)

TAT=[]
for i in range(0,len(pid)):
    TAT.append(completion[i]-arrival[i])

wait=[]
for i in range(0,len(pid)):
    wait.append(TAT[i]-burst[i])

rd=[]
for i in range(0,len(pid)):
    rd.append(TAT[i]/burst[i])

print("\n\nWaiting time")
for i in range(0,len(pid)):
    print("Process num",i,"=",wait[i])
print("\nAverage WT=", sum(wait)/len(wait))

print("\n\nTurnaround time")
for i in range(0,len(pid)):
    print("Process num",i,"=",TAT[i])
print("\nAverage TAT=", sum(TAT)/len(TAT))

print("\n\nRelative delay")
for i in range(0,len(pid)):
    print("Process num",i,"=",rd[i])
print("\nAverage RD=", sum(rd)/len(rd))


