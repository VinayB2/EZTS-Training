def findWinner(lst):
    sorted(lst)
    # frequency of votes
    vote_count = {}
    for i in lst:
        if i not in vote_count:
            vote_count[i] = 1
        else:
            vote_count[i] += 1

    votes = []
    for i in vote_count:
        votes.append(vote_count[i])

    winner = -1
    count = 0

    for i in vote_count:
        if vote_count[i] > count:
            count = vote_count[i]
            winner = i
    candidte = votes.index(count)
    votes.pop(candidte)
    if count in votes:
        return -1
    else: return winner   
lst = [1, 2, 2, 3, 5, 6, 4, 3, 3, 2]
print(findWinner(lst))