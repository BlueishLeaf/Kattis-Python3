dice = input().split()
die1 = int(dice[0])
die2 = int(dice[1])
if die1 > die2:
    die1 = die1^die2
    die2 = die2^die1
    die1 = die1^die2
for x in range(die1+1, die2+2):
    print(x)