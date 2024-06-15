moves = [1, -1, 1, -1, 1]
sum = 0
count = 0
for i in moves:
    sum += i
    if sum == 0:
        count += 1
print(count)