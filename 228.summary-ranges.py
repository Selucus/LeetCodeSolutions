#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sol = []
        if nums == []:
            return []
        start = nums[0]
        prev = nums[0]
        
        for item in nums[1:]:
            if item-prev != 1:
                if start == prev:
                    sol.append(str(start))
                else:
                    sol.append(str(start)+"->"+str(prev))
                start = item
                prev = item
            else:
                prev = item
        if start == prev:
            sol.append(str(start))
        else:
            sol.append(str(start)+"->"+str(prev))
        return sol


        
# @lc code=end

