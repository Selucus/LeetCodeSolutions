#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # find mins
        mins = []
        rowindex = 0
        while rowindex < len(matrix):
            colindex = 0
            minindex = 0
            minimum = float("inf")
            while colindex < len(matrix[rowindex]):
                if matrix[rowindex][colindex] < minimum:
                    minimum = matrix[rowindex][colindex]
                    minindex = colindex
                colindex += 1
            mins.append((rowindex,minindex))
            rowindex += 1
        maxes = []
        colindex=0
        while colindex < len(matrix[0]):
            rowindex = 0
            maxindex = 0
            maximum = float("-inf")
            while rowindex < len(matrix):
                if matrix[rowindex][colindex] > maximum:
                    maximum = matrix[rowindex][colindex]
                    maxindex = rowindex
                rowindex += 1
            maxes.append((maxindex,colindex))
            colindex += 1
        sol = []
        for item in mins:
            if item in maxes:
                sol.append(matrix[item[0]][item[1]])

        return sol




        
# @lc code=end

