names=input().split('-')
initials=[]
for name in names:
    initials.append(name[0])
print(''.join(initials))