def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def findMin(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min
print(findMin([2,5,4,2,4,5,3,1]))