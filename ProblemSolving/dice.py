faces = list(map(int, input().split()))
p1 = 0
p2 = 0
current = "p1"
for i in faces:
    
    if current == "p1":
        p1 += i
    