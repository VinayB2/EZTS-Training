def findMissing(lst):
    max = sorted(lst)[len(lst) - 1]
    for i in range(max + 1):
        if i not in lst:
            return i
    return -1

print(findMissing([1,3,4,5,0]))