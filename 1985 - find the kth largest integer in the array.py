# solve using a min-heap
# going to write heap logic myself but heapq module is more efficient

nums = ["3","6","7","10"]
k = 4
nums = [int(x) for x in nums]
import heapq

hq = nums[:k]
heapq.heapify(hq)
print(hq)
i = k
while i < len(nums):
    if(nums[i]<hq[0]):
        heapq.heapreplace(hq,nums[i])

    i += 1

print(hq[0])