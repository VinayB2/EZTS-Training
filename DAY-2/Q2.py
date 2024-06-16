def find_equilibrium(lst):
    for n in range(len(lst)):
        left = lst[0:n]
        right = lst[n:len(lst)]
        if sum(left) == sum(right): return n
    return len(lst) // 2
def find_gates(check_pts):
    gates = []
    for pt in check_pts: gates.append(find_equilibrium(pt)) 
    return gates
def get_ans(checkpoints):
    dic = {}
    for i in checkpoints: dic[str(i)] = find_equilibrium(i)
    pretty_print(dic)
def pretty_print(dic):
    k = 1
    for i, j in dic.items():
        print("Checkpoint ",k,": ", j)
        k += 1
checkpoints = [[2,2,1,2,1], [4,2,3,1,2,1,2,3], [1,1,1,1,1], [3,0,3], [1,2,1,1,2,1], [1,1,1,2,1], [5,2,1,3,1,2,5]]
get_ans(checkpoints)