def is_palindrome(num):
    temp = list(str(num))
    i = 0
    j = len(temp) - 1
    while i < j:
        if temp[i] != temp[j]:
            return False
        i += 1
        j -= 1
    return True
print(is_palindrome(12213))