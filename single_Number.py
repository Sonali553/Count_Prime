lst = list(map(int, input().split()))
def single_Number(lst):
    res = 0
    for i in range(0, len(lst)):
        res = res ^ lst[i]
    return res
print(single_Number([1, 2, 2, 3, 1]))
print(single_Number([1, 2, 2]))
print(single_Number(lst))