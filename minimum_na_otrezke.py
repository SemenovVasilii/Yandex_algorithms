N, M = map(int, input().split())
all_list = list(map(int, input().split()))
pairs = []
for j in range(M):
    L, R = map(int, input().split())
    pairs.append([L, R])
for i in pairs:
    maximum_num = -10000000
    minimum_num = 10000000
    for k in range(i[0], i[1] + 1):
        if all_list[k] > maximum_num:
            maximum_num = all_list[k]
        if all_list[k] < minimum_num:
            minimum_num = all_list[k]
    if maximum_num != minimum_num:
        print(maximum_num)
    else:
        print("NOT FOUND")