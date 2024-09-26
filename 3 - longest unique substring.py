s = "abcabcbb"

# solve using 2 pointer method
# use a set to record characters currently in substring

inSub = {s[0]}
i = 0
j = 1
count = 1
longest = 1
while j < len(s):
    if(s[j] not in inSub):
        count += 1
        longest = max(count,longest)
        inSub.add(s[j])
        j += 1
    else:
        inSub.remove(s[i])
        count -= 1
        i += 1
        
print(longest)