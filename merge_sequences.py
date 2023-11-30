x = int(input())
def get_num(x):
    n = 1
    i = 2
    k = 2
    otv = 1
    while x > n:
        if i**2 == k**3:
            otv = i**2
            k += 1
            i += 1
            n += 1
            continue
        if i**2 < k**3:
            otv = i**2
            i += 1
            n += 1
        else:
            otv = k**3
            k += 1
            n += 1
    return otv

print(get_num(x))