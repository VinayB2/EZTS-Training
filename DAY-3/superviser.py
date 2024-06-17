from Stack import Stack
def findMax(workers, worker, i):
    for i in range(i, len(workers)):
        if workers[i] > worker:
            return workers[i]
    return -1
def get_supervisers(workers):
    supervisers = Stack()
    i = 0
    for worker in workers:
        max = findMax(workers, worker, i)
        supervisers.push(max)
        i+=1
    return supervisers



def get_supervisers2(workers):
    stack = Stack()
    for i in range(len(workers)):
        i = -(i+1)
        if stack.isEmpty():
            workers[i] = -1
            stack.push(workers[i])
        elif stack.peek() > workers[i]:
            current = workers[i]
            workers[i] = stack.peek()
            stack.push(current)
        elif stack.peek() < workers[i]:
            ele = stack.pop()
            while ele < workers[i] and not stack.isEmpty():
                ele = stack.pop()            
    return workers


print(get_supervisers2([3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]))
