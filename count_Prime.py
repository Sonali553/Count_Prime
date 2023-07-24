def count_Prime(r):
    res = 0
    for num in range(2, r + 1):
        f = 0
        for i in range(2, num):
            if num % i == 0:
                f = 1
                break
        if f == 0:
            res += 1
            print(num)
    return res
print(count_Prime(10))
print(count_Prime(0))
print(count_Prime(1))
