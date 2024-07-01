hashTable = {}
def hash(val):
    f1 = val % 11
    if f1 not in hashTable: 
        hashTable[f1] = val
        return f1
    f2 = 8 - (val % 8)
    i = 1
    f3 = (f1 + i*f2) % 11
    while f3 in hashTable:
        i += 1
        f3 = (f1 + i*f2) % 11
    hashTable[f3] = val
    return f3

nums = [20, 34, 45, 70, 56, 81, 104, 37, 46, 39]
for i in nums:
    hash(i)
print(hashTable)

global hashList
hashList = []
def hash(val):
    f1 = val % 11
    if not hashList[f1]:
        hashList[f1] = val
        return f1
    f2 = 8 - (val % 8)
    i = 1
    f3 = (f1 + i*f2) % 11
    while hashList[f3]:
        i += 1
        f3 = (f1 + i*f2) % 11
    hashList[f3] = val
    return f3

nums = [20, 34, 45, 70, 56, 81, 104, 37, 46, 39]
def createHashTable(nums):
    global hashList
    hashList = [None] * len(nums)
    for i in nums:
        hash(i)
    print(hashList)
createHashTable(nums)