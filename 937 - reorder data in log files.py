# thinking about using merge sort implementation with the custom comparison 


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    leftSorted = merge_sort(left)
    rightSorted = merge_sort(right)

    return merge(leftSorted,rightSorted)

def merge(l,r):
    res = []

    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if(compare(l[i],r[j])):
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    while i < len(l):
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1
    return res
def compare(first,second):
    # comparison function that returns true if first < second
    # letter before dig
    if first[-1].isdigit() and (not second[-1].isdigit()):
        return False
    elif (not first[-1].isdigit()) and second[-1].isdigit():
        return True
    else:
        # same type
        if first[-1].isdigit():
            return True
        else:
            i = 0
            j = 0
            firstID = ""
            secondID = ""
            while first[i] != " ":
                firstID += first[i]
                i += 1

            while second[j] != " ":
                secondID += second[j]
                j += 1
            i += 1
            j += 1

            # at start of first word
            while i < len(first) and j < len(second):
                if first[i] == " " and second[j] == " ":
                    pass
                elif first[i] == " ":
                    return True
                elif second[j] == " ":
                    return False
                elif first[i] < second[j]:
                    return True
                elif second[j] < first[i]:
                    return False
                i += 1
                j += 1
            if i == len(first) and j != len(second):
                return True
            elif j == len(second) and i != len(first):
                return False
            else:
                return firstID < secondID
                
            

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(merge_sort(logs))

    