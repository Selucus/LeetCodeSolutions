#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        letters = {}
        for char in magazine:
            try:
                letters[char] += 1
            except:
                letters[char] = 1
        print(letters)
        for char in ransomNote:
            try:

                letters[char] -= 1
                if letters[char] < 0:
                    return False
            except:
                return False

        return True"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        letters = [0] * 26
        for char in magazine:
            letters[ord(char)-97] += 1
        
        for char in ransomNote:
            i = ord(char) - 97
            letters[i] -= 1
            if letters[i] < 0:
                return False

        return True
# @lc code=end

