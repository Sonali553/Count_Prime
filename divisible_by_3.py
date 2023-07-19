Array = list(map(int, input().split()))
def divisible_by_3(Array):
    ans = 0
    S = 1
    n=len(Array)
    while(n):
        ans = ans + ((Array[n-1] % 3 * S)) % 3

        S = (S * 10) % 3
        n = n - 1
    return 1 if ans % 3 == 0 else 0
print(divisible_by_3([1, 2, 3]))
print(divisible_by_3([1, 0, 0, 1, 2]))
print(divisible_by_3(Array))