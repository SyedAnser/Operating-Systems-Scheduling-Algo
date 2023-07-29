import numpy

with open('C:/Users/syeda/Desktop/codes/fcfs.txt') as f:
    z=[]
    for line in f:
        line = line.split() # to deal with blank 
        line = [int(i) for i in line]
        z.append(line)

def Non_Preemptive_LJF():
    pid1=z[0]
    burst1=z[1]
    arrival1=z[2]
    state=z[3]

    pid=[]
    burst=[]
    arrival=[]

    Gantt=[]

    s = numpy.array(arrival1)
    sort_index = numpy.argsort(s)

    for i in sort_index:
        pid.append(pid1[i])
        burst.append(burst1[i])
        arrival.append(arrival1[i])

    time=0
    end=[]
    q_ready=[]
    t=[]
    completed=0

    while completed<len(pid):
        for i in range(len(pid)):
            if arrival[i]<=time and state[i]==0:
                t.extend([pid[i], arrival[i], burst[i]])
                q_ready.append(t)
                t=[]
        
        if len(q_ready)==0:
            time+=1
        
        while len(q_ready)!=0:
            q_ready.sort(key=lambda x:x[2])
            q_ready.reverse()
            x=q_ready[0]
            for i in range(x[2]):
                Gantt.append(x[0])
                time+=1
            index=pid.index(x[0])
            state[index]=1
            completed+=1
            t.extend([x[0],time])
            end.append(t)
            t=[]
            q_ready.remove(x)
            


    completion=[]
    TAT=[]
    Waiting=[]
    RD=[]
        
    print("\nGantt Chart:", Gantt)

    for i in pid:
        for j in range(len(end)):
            if i==end[j][0]:
                completion.append(end[j][1])

    for i in range(len(pid)):
        TAT.append(completion[i]-arrival[i])

    for i in range(len(pid)):
        Waiting.append(TAT[i]-burst[i])

    for i in range(len(pid)):
        RD.append(TAT[i]/burst[i])

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
    




def Preemptive_LJF():
    pid1=z[0]
    burst1=z[1]
    arrival1=z[2]
    state=z[3]

    pid=[]
    burst=[]
    arrival=[]

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

    burst2=burst.copy()

    completed=0

    while completed<len(pid):
        q_ready=[]
        q=[]
        t=[]
        for i in range(len(pid)):
            if arrival[i]<=start_time and state[i]==0:
                t.extend([pid[i], arrival[i], burst[i]])
                q_ready.append(t)
                t=[]
            elif state[i]==0:
                t.extend([pid[i], arrival[i], burst[i]])
                q.append(t)
                t=[]
        if len(q_ready)==0 and len(q)==0:
            break
        if len(q_ready)!=0:
            q_ready.sort(key=lambda x:x[2])
            q_ready.reverse()
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


choice=int(input("Make your choice:\n1) Non-Preemptive\n2) Preemptive\n"))
if choice==1:
    Non_Preemptive_LJF()
elif choice==2:
    Preemptive_LJF()
