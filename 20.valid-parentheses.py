#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'(':')','{':'}','[':']'}
        open = list(valid.keys())
        for char in s:
            if char in open:
                stack.append(char)
            else:
                try:
                    n = stack.pop()
                except:
                    return False
                if valid[n] != char:
                    return False
        if len(stack)==0:

            return True    
        else:
            return False
        
# @lc code=end

