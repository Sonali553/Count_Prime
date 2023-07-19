A, B = map(int, input().split())
def set_bit(A, B):
    if A == B:
        return  (2 **(A))
    return  (2 **(A)) +  (2 **(B))
print(set_bit(4, 4))
print(set_bit(3, 5))
print(set_bit(A, B))
