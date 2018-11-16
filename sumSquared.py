numCases = int(input())
for i in range(1,numCases+1):
    data = input().split()
    b=int(data[1])
    n=int(data[2])
    ssd=0
    while(n>0):
        ssd+=(n%b)*(n%b)
        print(ssd)
        n = n / b
    print(ssd)
