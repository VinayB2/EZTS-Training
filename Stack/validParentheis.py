from Stack import Stack
# Approach 1
def isValid(exp):
    stack = Stack()
    o = '([{'
    c = ')]}'
    for i in exp:
        if i in o:
            if i == '[':
                stack.push('[')
            elif i == '(':
                stack.push('(')
            else:
                stack.push('{')
        elif i in c:
            if stack.size() == 0:
                return False
            if i == ')':
                stack.pop()
            elif i == ']':
                stack.pop()
            elif i == '}':
                stack.pop()
    return stack.isEmpty()
# Approach 2
def isValid2(exp):
    freq = {}
    o = '([{'
    c = ')]}'
    for i in exp:
        if i in o:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        elif i in c:
            if i == ']':
                freq['['] -= 1
            if i == ')':
                freq['('] -= 1
            if i == '}':
                freq['{'] -= 1
    for key, val in freq.items():
        if val != 0:
            return False
    return True
# Approach 3
def isValid3(exp):
    b = "({[]]})"
    brackets = ""
    for i in exp:
        if i in b:
            brackets += i
    if len(brackets) %2 != 0: return False
    i = 0
    j = len(brackets) - 1
    brackets = brackets.replace(']', '[')
    brackets = brackets.replace(')', '(')
    brackets = brackets.replace('}', '{')
    while i < j:
        if brackets[i] != brackets[j]: return False
        i+=1
        j-=1
    return True

print(isValid3("[3+7{52/11(3+5)})]"))