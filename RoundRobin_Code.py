import numpy as numpy

with open('C:/Users/syeda/Desktop/codes/round robin.txt') as f:
    x=[]
    for line in f:
        line = line.split() # to deal with blank 
        line = [int(i) for i in line]
        x.append(line)

pid=x[0]
burst=x[1]

burst1=burst.copy()

Gantt=[]

tq=int(input("Enter time quantum:"))

while len(Gantt)<sum(burst1):
    for i in range(len(burst)):
        if burst[i]>tq:
            burst[i]-=tq
            for j in range(tq):
                Gantt.append(pid[i])
        else:
            x=burst[i]
            burst[i]=0
            for j in range(x):
                Gantt.append(pid[i])

print("\nGantt=", Gantt)

complete_time=[]
for i in (pid):
    complete_time.append(len(Gantt)-Gantt[::-1].index(i))

turnaround_time=[]
for i in range(0,len(pid)):
    turnaround_time.append(complete_time[i])

waiting_time=[]
for i in range(0,len(pid)):
    waiting_time.append(turnaround_time[i]-burst1[i])

rel_delay=[]
for i in range(0,len(pid)):
    rel_delay.append(turnaround_time[i]/burst1[i])

print("\n\nWaiting Time:")
for i in range(0,len(pid)):
    print("Process num",i,"=",waiting_time[i])
print("\nAverage WT=", sum(waiting_time)/len(waiting_time))

print("\n\nTurnaround time")
for i in range(0,len(pid)):
    print("Process num",i,"=",turnaround_time[i])
print("\nAverage turnaround_time=", sum(turnaround_time)/len(turnaround_time))

print("\n\nRelative delay")
for i in range(0,len(pid)):
    print("Process num",i,"=",rel_delay[i])
print("\nAverage RD=", sum(rel_delay)/len(rel_delay))


