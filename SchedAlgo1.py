import csv
import pandas as pd
df=pd.read_csv("fcfs.txt",sep="\t")
df2=df.sort_values(by='Arrival Time')
df2=df2.reset_index(drop=True)
bt=df2['Burst Time']
print("Given data: ",'\n',df.to_string(index=False))
chart=0
gc=[]
for i in range(0,len(bt)):
    chart=bt[i]+chart
    gc.append(chart)
print("Gannt Chart: ", gc)
wait=[0]
for i in range(0,len(gc)-1):
    wait.append(gc[i])
Tat=[]
for i in range(0,len(wait)):
    Tat.append(bt[i]+wait[i])
rd=[]
for i in range(len(Tat)):
    rd.append(Tat[i]/bt[i])
df2['TurnAroundTime']=Tat
df2['Waiting Time']=wait
df2['Response Time']=wait
df2['Relative Delay']=rd
print(df2.to_string(index=False))
for i in range(len(Tat)):
    sum=+Tat[i]
for i in range(len(wait)):
    sum1=+wait[i]
for i in range(len(rd)):
    sum2=+rd[i]
print("Average Turn Around Time: ", sum/len(Tat))
print("Average Waiting Time: ", sum1/len(wait))
print("Average Relative Delay: ", sum2/len(rd))
