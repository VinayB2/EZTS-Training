def CalculateBinaryOperation(string):
    if not string: return -1
    op1 = 0
    opr = 1
    op2 = 2
    while op2 <= len(string) - 1:
        ans = 0
        if string[opr] == 'A':
            ans = int(string[op1]) and int(string[op2])
        if string[opr] == 'B':
            ans = int(string[op1]) or int(string[op2])
        if string[opr] == 'C':
            ans = int(string[op1]) ^ int(string[op2])
        string = string[3:]
        string = str(ans) + string
    return string
print(CalculateBinaryOperation(""))