def sum(list=[]):
    s = 0
    for num in list:
        s += num
    return s

def average(list=[]):
    s = sum(list)
    return s / len(list)
