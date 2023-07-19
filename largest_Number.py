from functools import cmp_to_key
lst = list(map(int, input().split()))
def largest_Number(lst):
    l = [str(ele) for ele in lst]
    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1
    lst = sorted(l, key = cmp_to_key(compare))
    return str(int("".join(lst)))
print(largest_Number([3, 30, 34, 5, 9]))
print(largest_Number([2, 3, 9, 0]))