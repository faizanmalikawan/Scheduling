f=open("process.txt")
print("Process No\tBurst Time\t Arrival Time\tWaiting Time\tTurnaround Time")
ProcessNo=[]
ArrivalTime=[]
BurstTime=[]
for index in range(3):
	ProcessNo[index]=f.read(2)
	read=f.read(2)
	ArrivalTime[index]=int(read)
	read=f.read(2)
	BurstTime[index]=int(read)
WaitingTime=[]
TurnaroundTime=[]
WaitingTime[0]=0
for index in range(1,3):
	WaitingTime[index]=BurstTime[index-1]+WaitingTime[index-1]
for index in range(3):
	TurnaroundTime[index]=BurstTime[index]+WaitingTime[index]
for index in range(3):
	print(ProcessNo[index],'\t',ArrivalTime[index],'\t', BurstTime[index],'\t',WaitingTime[index],'\t',TurnaroundTime[index])
TotalTurnaroundTime=0
for index in range(3):
	TotalTurnaroundTime=TotalTurnaroundTime+TurnaroundTime[index]
TotalWaitingTime=0
for index in range(3):
	TotalWaitingTime=TotalWaitingTime+WaitingTime[index]
print("Averge Waiting Time")
print(TotalWaitingTime/3)
print("Average Turnaround Time")
print(TotalTurnaroundTime/3)