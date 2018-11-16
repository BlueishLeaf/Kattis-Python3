numCases=int(input())
total = 0
for x in range (0, numCases):
    ab=input().split()
    total+=float(ab[0])*float(ab[1])
print(total)