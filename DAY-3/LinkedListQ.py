def evaluate(exp):
    ops = ['+', '-', '*', '/',  '%']
    opr = ''
    for i in exp:
        if i in ops:
            opr = i
            break
        
    if opr == '*':
        count = exp.count('*')
        if count > 1:
            expr = exp.replace(opr, " ")
            print(type(expr))
            expr = list(map(float, expr)) 
            return expr[0] ** expr[1]

    expr = exp.split(opr)
    expr = list(map(float, expr))
    if opr == '+': return expr[0] + expr[1]
    if opr == '-': return expr[0] - expr[1]
    if opr == '*': return expr[0] * expr[1]
    if opr == '/': return expr[0] / expr[1]
    if opr == '%': return expr[0] % expr[1]
print(evaluate('3 ** 4'))