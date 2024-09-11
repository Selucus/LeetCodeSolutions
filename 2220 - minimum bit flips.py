start = 10
goal = 7
import math
# think about doing some maths to solve this, obvious solution is convert to binary and iterate through comparing digits
changes  = 0
curDiv =2**math.ceil(math.log2(max(start,goal)))
while curDiv >= 1:
    if curDiv <= start and curDiv <= goal:
        start-= curDiv
        goal-=curDiv
    elif curDiv <= start:
        start -= curDiv
        changes +=1
    elif curDiv <= goal:
        changes += 1
        goal -= curDiv
    curDiv /= 2


print(changes)