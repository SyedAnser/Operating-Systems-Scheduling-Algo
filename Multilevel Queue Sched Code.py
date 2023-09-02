import numpy

with open('C:/Users/syeda/Desktop/codes/mqs.txt') as f:
    z=[]
    for line in f:
        line = line.split() # to deal with blank 
        line = [int(i) for i in line]
        z.append(line)


pid1=z[0]
burst1=z[1]
arrival1=z[2]

pid=[]
burst=[]
arrival=[]

s = numpy.array(arrival1)
sort_index = numpy.argsort(s)

for i in sort_index:
    pid.append(pid1[i])
    burst.append(burst1[i])
    arrival.append(arrival1[i])

time=0
tq=8
Gantt=[]

for i in range(len(pid)):
    if burst[i]>tq:
        burst[i]-=tq
        time+=8
        for j in range(tq):
            Gantt.append(pid[i])
    else:
        x=burst[i]
        burst[i]=0
        time+=tq
        for j in range(x):
            Gantt.append(pid[i])


tq=16

for i in range(len(pid)):
    if burst[i]>tq:
        burst[i]-=tq
        time+=tq
        for j in range(tq):
            Gantt.append(pid[i])
    else:
        x=burst[i]
        burst[i]=0
        time+=x
        for j in range(x):
            Gantt.append(pid[i])


for i in range(len(pid)):
    for j in range(burst[i]):
        Gantt.append(pid[i])
        time+=1


print("\nGantt=", Gantt)

complete_time=[]
for i in (pid):
    complete_time.append(len(Gantt)-Gantt[::-1].index(i))

turnaround_time=[]
for i in range(0,len(pid)):
    turnaround_time.append(complete_time[i]-arrival[i])

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


