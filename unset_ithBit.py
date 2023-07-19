A, B = map(int, input().split())
def unset_ith_Bit(A, B):
   
    if(A & (1 << B)):
        return  A ^ (1 << B)
    return A

print(unset_ith_Bit(4, 1))
print(unset_ith_Bit(5, 2))
print(unset_ith_Bit(A, B))
 
