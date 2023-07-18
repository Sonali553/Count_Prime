num, B = map(int, input().split())
def checkBit(num, B):
    if(num & (1 << B)):
        return 1
    return 0
print(checkBit(4, 1))
print(checkBit(5, 2))
print(checkBit(num, B))