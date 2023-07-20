def find_Factorial(N):
    if N <= 1:
        return 1
    return find_Factorial(N - 1) * N
print(find_Factorial(5))