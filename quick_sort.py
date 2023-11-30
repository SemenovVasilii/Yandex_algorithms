import random
import sys
sys.setrecursionlimit(2**30)
num = int(input())
array = list(map(int, input().split()))

def partition(arr, start, stop):
    e, g, n = arr[start], start, stop
    i = g
    while i <= n:
        if arr[i] < e:
            arr[i], arr[g] = arr[g], arr[i]
            g += 1
        elif arr[i] > e:
            arr[i], arr[n] = arr[n], arr[i]
            n -= 1
            i -= 1
        i += 1
    return g, n

def quicksort(arr, start, stop):
    if start >= stop:
        return
    else:
        pivot = random.randint(start, stop)
        arr[start], arr[pivot] = arr[pivot], arr[start]
        p1, p2 = partition(arr, start, stop)
        quicksort(arr, start, p1 - 1)
        quicksort(arr, p2 + 1, stop)


quicksort(array, 0, len(array) - 1)
print(*array)