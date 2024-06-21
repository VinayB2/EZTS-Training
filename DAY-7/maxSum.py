import math
def maxSum(n):
    maximum = -1*math.inf
    for i in range(len(n)):
        for j in range(i, len(n)):
            maximum = max(maximum, sum(n[i:j]))
    return maximum
print(maxSum([4, -1, -3, 6, -2, -1, 3, 2, -8, -2]))