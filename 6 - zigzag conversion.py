s = "PAYPALISHIRING"
numRows = 3
# Use math on string indexes to solve
if(numRows == 1):
    print(s)
output = ""
for i in range(numRows):
    down = (2*(numRows-i)) - 2
    up = (2*(i+1)) - 2
    goingDown = True
    cur = i
    print(numRows,up,down)
    while cur < len(s):

        
        if(goingDown):
            if(down>0):
                output += s[cur]
                cur += down
        else:
            if(up>0):
                output += s[cur]
                cur += up
        goingDown = not goingDown
    
print(output)
