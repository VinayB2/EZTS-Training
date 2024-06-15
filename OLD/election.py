l=list(map(int, input().split(' ')))
count = [0]*(max(l))
for i in l:
    count[i - 1] = count[i - 1] + 1
print(count)
print(max(count) - 1)