def find_max_sum(arr):
    max = 0
    lst = []
    for i in range(len(arr) - 2):
        temp = sum(arr[i:i+3])
        if max < temp: 
            max = sum(arr[i:i+3])
            lst = arr[i:i+3]
    return lst

# For k consecutive terms
def find_max_sum2(arr, k):
    max = 0
    lst = []
    for i in range(len(arr) - k + 1):
        temp = sum(arr[i:i + k])
        if max < temp: 
            max = sum(arr[i:i + k])
            lst = arr[i:i+k]
    return lst
def find_max_sum3(arr, k):
    window = max = 0
    for i in range(0, k):
        window += arr[i]
    for i in range(0, len(arr) - k - 1):
        if max < window:
            max = window
        window = window + arr[i + k] - arr[i]
    return max

print(find_max_sum3([2,3,4,5,1,5,6,7,5,2], 4))