prices = [7,1,5,3,6,4]
# sliding window solution

maxProfit = 0
curCheapest = float("inf")

for i in prices:
    curCheapest = min(i,curCheapest)
    maxProfit = max(maxProfit,i-curCheapest)
    
print(maxProfit)