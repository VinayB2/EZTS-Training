n = int(input())
arr = list(map(int, input().split()))
found = False
for i in range(n):
    if sum(arr[:i]) == sum(arr[i + 1:]): 
        print(i + 1)
        found = True
if not found: print("NOT FOUND")