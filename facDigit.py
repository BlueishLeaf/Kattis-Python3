import math

numCases = int(input())
ouputs = []
for i in range(0,numCases):
    value = int(input())
    fac = math.factorial(value)
    facStr = str(fac)
    ouputs.append(facStr[-1])
for x in ouputs:
    print(x)