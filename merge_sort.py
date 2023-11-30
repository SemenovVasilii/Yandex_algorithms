num = int(input())
arr = list(map(int, input().split()))
def merge(arr1, arr2):
    finish = []
    cnt1 = cnt2 = 0
    while cnt1 < len(arr1) and cnt2 < len(arr2):
        if arr1[cnt1] <= arr2[cnt2]:
            finish.append(arr1[cnt1])
            cnt1 += 1
        else:
            finish.append(arr2[cnt2])
            cnt2 += 1
    if cnt1 < len(arr1):
        finish += arr1[cnt1:]
    if cnt2 < len(arr2):
        finish += arr2[cnt2:]
    return finish
def sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    mid = len(arr) // 2
    right = sort(arr[mid:])
    left = sort(arr[:mid])
    return merge(left, right)

print(*sort(arr))