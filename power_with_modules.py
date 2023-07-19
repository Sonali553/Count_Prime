A, P, C = map(int, input().split())
def powerModulus(A, P, C):
    res = 1
    for i in range(P):
        A = A % C
        res = (res * A) % C
    return res
print(powerModulus(2, 3, 3))
print(powerModulus(5, 2, 4))
print(powerModulus(A, P, C))