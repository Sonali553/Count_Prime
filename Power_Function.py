def powmod(a, n, m):
    if(n == 0):
        return 1
    if n == 1:
        return a
    p = powmod(a, n//2, m)
    if(n % 2 == 0):
        return (p * p) % m
    else:
        return (p * p * a) % m
print(powmod(2, 3, 3))
print(powmod(3, 3, 2))
print(powmod(2, 5, 7))