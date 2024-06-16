#  get the frequency of maximum vowel in the sentense spoken by each
def find_max_freq_vovel(sentence):
    freq = {}
    vovels = ['a', 'e', 'i', 'o', 'u']
    sentence = sentence.replace(" ", "").lower()
    for i in sentence:
        if i not in vovels: continue
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_count = max(freq.values())
    lst = []
    for item, count in freq.items():
        if count == max_count:
            lst_ = [item, count]
            lst.append(lst_)
    return lst
def winner(statements):
    lst = []
    for i in statements:
        vov_freq = find_max_freq_vovel(i[1])
        lst_ = [i[0], vov_freq[0][0]]
        n = 1
        if len(vov_freq) > 1:
            lst_.append(vov_freq[n][0])
            n += 1
        lst.append(lst_)
    return lst
def winner2(statements):
    dic = {}
    for i in statements:
        dic[i[0]] = find_max_freq_vovel(i[1])[0][0]
    return dic
statements = [
    ["Alex", "I enjoy hiking to the mountain"],
    ["sam", "A lovely sunny day at the beach"],
    ["jamie", "reading a book is my favorite pastime"],
    ["taylor", "I love playing video games on weekends"],
    ["chris", "Exploring new cities is exciting and fun"],
    ["test", "eeeaaa"]
]
print(winner2(statements))