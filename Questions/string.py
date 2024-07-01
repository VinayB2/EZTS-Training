def check(string, seq):
    indices = []
    for i in range(len(string)):
        if string.startswith(seq):
            indices.append(i)
        string = string[1:]
    return indices
print(check('ABABABCANFKABABCNKABABCACNDA', 'ABABCA'))