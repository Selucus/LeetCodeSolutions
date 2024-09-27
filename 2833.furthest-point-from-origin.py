#
# @lc app=leetcode id=2833 lang=python3
#
# [2833] Furthest Point From Origin
#

# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0
        either = 0
        for char in moves:
            if char == "L":
                l += 1
            elif char == "R":
                r += 1
            else:
                either += 1
        return abs(l-r) + either

        
    

   

# @lc code=end

