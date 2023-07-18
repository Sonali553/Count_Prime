n, b = map(int, input().split())
def decimal_ToBase(n, b):
    res = ''
    if n == 0:
        return 0
    while(n > 0):
        r = n % b
        res = str(r) + res
        n = n // b
    return int(res)

print(decimal_ToBase(4, 3))
print(decimal_ToBase(4, 2))
print(decimal_ToBase(n, b))