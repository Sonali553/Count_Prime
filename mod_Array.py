Array = list(map(int, input().split()))
P = int(input())
def mod_Array(A, P):
    ans = 0
    S = 1
    n=len(Array)
    while(n):
        ans = ans + ((Array[n-1] % P * S)) %P

        S= (S * 10) % P
        n=n-1
    return ans % P
print(mod_Array([1,4,3],2))
print(mod_Array(Array, P))