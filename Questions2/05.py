def hyphens(string):
    hyp = ""
    nhyp = ""
    for i in string:
        if i == '-': hyp += i
        else: nhyp += i
    return hyp + nhyp
print(hyphens('hello-world'))