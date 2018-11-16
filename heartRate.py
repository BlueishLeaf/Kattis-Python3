numCases = int(input())
for x in range(0,numCases):
    data=input().split()
    b=int(data[0])
    p=float(data[1])
    bpm=(60*b)/p
    print(str(round(bpm-(60.0/p),4)) + ' ' + str(round(bpm,4)) + ' ' + str(round(bpm+(60.0/p),4)))