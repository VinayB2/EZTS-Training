def generate_fibo(num):
    fibo = [0]
    i = 0
    j = 1
    if num <= 1: return fibo
    fibo.append(j)
    if num <= 2: return fibo
    for k in range(num - 2):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo
def generate_fibo2(num):
    # complexity : O(N)
    fibo = [0]
    i = 0
    j = 1
    for k in range(num - 1):
        c = i + j
        fibo.append(c)
        i = j
        j = c
    return fibo
def is_fibo(num):
    # time complexity : O(N)
    # space complexity  : O(N)
    if num < 0: return False
    fibo = []
    i = 0
    j = 1
    while True:
        c = i + j
        fibo.append(c)
        i = j
        j = c
        if fibo[len(fibo) - 1] == num:
            return True
        if fibo[len(fibo) - 1] > num:
            return False

print(is_fibo(1597))