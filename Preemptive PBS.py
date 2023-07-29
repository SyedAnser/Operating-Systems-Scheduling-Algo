
import numpy

with open('C:/Users/syeda/Desktop/codes/fcfs.txt') as f:
    z=[]
    for line in f:
        line = line.split() # to deal with blank 
        line = [int(i) for i in line]
        z.append(line)

def PBS():
    pid1=z[0]
    burst1=z[1]
    arrival1=z[2]
    state=z[3]
    priority1=z[4]

    pid=[]
    burst=[]
    arrival=[]
    priority=[]

    s = numpy.array(arrival1)
    sort_index = numpy.argsort(s)

    x=[]
    y=[]

    start=[]
    end=[]
    start_time=0
    Gantt=[]

    completion=[]
    TAT=[]
    Waiting=[]
    RD=[]

    for i in sort_index:
        pid.append(pid1[i])
        burst.append(burst1[i])
        arrival.append(arrival1[i])
        priority.append(priority1[i])

    burst2=burst.copy()

    completed=0

    while completed<len(pid):
        q_ready=[]
        q=[]
        t=[]
        for i in range(len(pid)):
            if arrival[i]<=start_time and state[i]==0:
                t.extend([pid[i], arrival[i], burst[i], priority[i]])
                q_ready.append(t)
                t=[]
            elif state[i]==0:
                t.extend([pid[i], arrival[i], burst[i], priority[i]])
                q.append(t)
                t=[]
        if len(q_ready)==0 and len(q)==0:
            break
        if len(q_ready)!=0:
            q_ready.sort(key=lambda x:x[3])
            start.append(start_time)
            start_time+=1
            end_time=start_time
            end.append(end_time)
            Gantt.append(q_ready[0][0])
            
            for j in range(len(pid)):
                if pid[j]==q_ready[0][0]:
                    break
            burst[j]=burst[j]-1
            if burst[j]==0:
                state[j]=1
                completed+=1
                x.append(pid[j])
                y.append(end_time)

        if len(q_ready)==0:
            if start_time<q[0][1]:
                start_time=q[0][1]
            start.append(start_time)
            start_time+=1
            end_time=start_time
            end.append(end_time)
            Gantt.append(q[0][0])
            for j in range(len(pid)):
                if pid[j]==q[0][0]:
                    break
            burst[j]=burst[j]-1
            if burst[j]==0:
                state[j]=1
                completed+=1
                x.append(pid(j))
                y.append(end_time)

    print("\nGantt Chart:", Gantt)

    for i in pid:
        for j in range(len(x)):
            if i==x[j]:
                completion.append(y[j])

    for i in range(len(pid)):
        TAT.append(completion[i]-arrival[i])

    for i in range(len(pid)):
        Waiting.append(TAT[i]-burst2[i])

    for i in range(len(pid)):
        RD.append(TAT[i]/burst2[i])

    print("\n\nWaiting time")
    for i in range(0,len(pid)):
        print("Process num",pid[i],"=",Waiting[i])
    print("\nAverage WT=", sum(Waiting)/len(Waiting))

    print("\n\nTurnaround time")
    for i in range(0,len(pid)):
        print("Process num",pid[i],"=",TAT[i])
    print("\nAverage TAT=", sum(TAT)/len(TAT))

    print("\n\nRelative delay")
    for i in range(0,len(pid)):
        print("Process num",i,"=",RD[i])
    print("\nAverage RD=", sum(RD)/len(RD))

PBS()