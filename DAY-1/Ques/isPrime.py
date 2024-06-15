def isPrime(num):
    if num <= 0: return False
    if num <= 2: return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

primes = []
for i in range(int(input("Prime numbers needed till: "))):
    if isPrime(i):
        primes.append(i)
print(primes)