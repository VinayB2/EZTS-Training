def countComma(n):
    count = 0
    for i in range(n + 1):
        # if i <= 999:
        #     continue
        count += getCommaCount2(i)
    return count
def getCommaCount(n):
    digits = 0
    while(n != 0):
        digits += 1
        n //= 1000
    return digits - 1
def getCommaCount2(n):
    digits = 0
    multiplier = 0
    while(n != 0):
        digits += multiplier * (n % 1000)
        multiplier += 1
        n //= 1000
    return digits
print(countComma(2000000))