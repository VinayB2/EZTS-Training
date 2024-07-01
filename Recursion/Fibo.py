def fibo(n):
    if n <= 2:
        return n
    return fibo(n - 1) + fibo(n - 2)
def fibo_seq(n):
    lst = []
    for i in range(n):
        lst.append(fibo(i))
    return lst


fibo_data = {0:0, 1:1, 2:2}
t = 0
def fiboDP(n):
    global t
    t+=1
    if n < 2:
        return fibo_data[n]
    if n in fibo_data:
        return fibo_data[n]
    fibo_data[n - 1] = fiboDP(n - 1)
    fibo_data[n - 2] = fiboDP(n - 2)
    return fibo_data[n - 1] + fibo_data[n - 2]

if __name__ == "__main__":
    print(fiboDP(50), t)