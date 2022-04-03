from collections import Counter

def median(data):
    return list(sorted(data))[len(data)//2]


def mode(data):
    c = Counter(data)
    return c.most_common(1)[0][0]


def mean(data):
    return sum(data) / len(data)


data = [1,2,3,3,4]
print(median(data))
print(mode(data))
print(mean(data))