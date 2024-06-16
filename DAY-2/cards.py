def find_min_cards(cards):
    picked = []
    pairs = 0
    for i in range(len(cards)):
        picked.append(cards[i])
        if pairs >= 1:
            return len(picked)
        if cards[i + 1] in picked:
            pairs += 1
    return - 1
def find_min_cards2(cards):
    picked = [cards[0]]
    for i in range(1, len(cards) - 1):
        picked.append(cards[i])
        if cards[i+1] in picked:
            picked.append(cards[i+1])
            return len(picked)
    return -1
print(find_min_cards2([3,4,2,3,4,7]))