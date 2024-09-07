nums = [2,2,1,1,1,2,2]

# Always a majority element (occurs more than n/2 times)
# find what it is

#hashmap solution
"""
n = len(nums)

seen = set()
counts = {}
numFound = 0
for item in nums:
    if(item in seen):
        newC = counts[item] + 1
        if(newC > n/2 - numFound):
            print(item)
        counts[item] = newC
    else:
        seen.add(item)
        counts[item] = 1
"""

# moore voting algorithm

count = 0
candidate = 0
for i in nums:
    if count == 0:
        candidate = i
        count += 1
    else:
        if i == candidate:
            count += 1
        else:
            count -= 1
print(candidate)


