cards=input().split()
ranks = []
rankCounts = []
tempcard=cards[0]
for card in cards:
    ranks.append(card[0])
for rank in ranks:
    rankCounts.append(ranks.count(rank))
rankCounts.sort(reverse=True)
print(rankCounts[0])
