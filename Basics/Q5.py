def no_of_problems_within(mins):
    probs = 0
    time_till_now = 0
    i = 1
    while time_till_now <= mins:
        time_till_now += 5 * i
        probs += 1
        i += 1
    return probs

def total_problems(start):
    time = (8 - start) * 60
    if time == 0: return 0
    return no_of_problems_within(time)

print(total_problems(int(input())))