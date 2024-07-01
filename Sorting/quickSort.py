def sort(arr):
    return helper(arr, 0, len(arr) - 1)
def helper(arr, low, high):
    if low < high:
        pi = findP(arr, low, high)
        helper(arr, low, pi - 1)
        helper(arr, pi +1, high)
    return arr
def findP(arr, low, high):
    p = high
    j = low - 1
    for i in range(high - 1):
        if arr[i] <= arr[p]:
            j += 1
            arr[p], arr[j] = arr[p], arr[j]
    j += 1
    arr[j], arr[p] = arr[p], arr[j]
    return p
print(sort([1,5,2,4,9,3]))