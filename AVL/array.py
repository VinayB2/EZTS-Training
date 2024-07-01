import math
def findminPos(arr):
    minimum = math.inf
    for i in arr:
        if i < arr[0] and i >= 1:
            minimum = i
    if minimum == 0: return -1
    return i
nums = [1,2,0]
for i in nums:
    if i <= 0:
        nums.remove(i)
print(nums)