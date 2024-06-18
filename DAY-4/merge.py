def merge(left, right):
    l = r = t = 0
    temp = [0]*(len(left) + len(right))
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            temp[t] = left[l]
            l += 1
        else:
            temp[t] = right[r]
            r += 1
        t += 1
    while l < len(left):
        temp[t] = left[l]
        t += 1
        l += 1 
    while r < len(right):
        temp[t] = right[r]
        r += 1
        t += 1
    return temp

def mergeSort(arr):
    if(len(arr) <= 1):
        return arr
    left = mergeSort(arr[0:len(arr)//2])
    right = mergeSort(arr[len(arr)//2:])
    return merge(left, right)

arr = [1,5,3,1,6,7]
print(mergeSort(arr))