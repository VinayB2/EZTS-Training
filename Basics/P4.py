def isPrime(N):
    if N <= 0: return False
    if N <= 2: return True
    for i in range(2, int(N // 2)):
        if N % i == 0: return False
    return True
# Level 1
def prime_greater_than_n(N):
    temp = N + 1
    while True:
        if isPrime(temp): return temp
        temp += 1
# Level 2
def sum_nums_between(N):
    next_prime = prime_greater_than_n(N)
    sum = 0
    for i in range(N + 1, next_prime):
        sum += i
    return sum
# level 3
def is_prduct_prime(N):
    next1 = prime_greater_than_n(N)
    next2 = prime_greater_than_n(next1)
    return isPrime(next1 * next2)
def prime_key(N):
    return (prime_greater_than_n(N), sum_nums_between(N), is_prduct_prime(N))
print(prime_key(int(input())))