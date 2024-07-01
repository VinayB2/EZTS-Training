m = 36
n = 5
arr = [9,18,2,1,4]
count = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] * arr[j] >= m: continue
        for k in range(j, len(arr)):
            if i == j == k: continue
            if arr[i] * arr[j] * arr[k] == m: 
                count += 1
print(count)